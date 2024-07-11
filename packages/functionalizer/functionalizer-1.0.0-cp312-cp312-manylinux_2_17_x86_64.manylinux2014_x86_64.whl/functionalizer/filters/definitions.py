"""Query interface for Neuron dataframe / graph."""

import hashlib
import importlib
import inspect
import os
import sys
from abc import abstractmethod
from datetime import datetime
from glob import glob
from pathlib import Path

import sparkmanager as sm

from functionalizer.circuit import Circuit
from functionalizer.utils import get_logger
from functionalizer.utils.checkpointing import checkpoint_resume

logger = get_logger(__name__)


def load(*dirnames: str) -> None:
    """Load plugins from a list of directories.

    If no directories are given, load a default set of plugins.

    Args:
        dirnames: A list of directories to load plugins from.
    """
    if not dirnames:
        dirnames = [os.path.join(os.path.dirname(__file__), "implementations")]
    for dirname in dirnames:
        filenames = glob(f"{dirname}/*.py")
        for filename in filenames:
            modulename = filename[:-3]
            relative = min((os.path.relpath(modulename, p) for p in sys.path), key=len)
            modulename = relative.replace(os.sep, ".")
            importlib.import_module(modulename)


# ---------------------------------------------------
# Dataset operations
# ---------------------------------------------------
class __DatasetOperationType(type):
    """Forced unification of classes.

    The structure of the constructor and application function to circuits
    is pre-defined to be able to construct and apply filters automatically.

    Classes implementing this type are automatically added to a registry,
    with a trailing "Filter" stripped of their name.  Set the attribute
    `_visible` to `False` to exclude a filter from appearing in the list.
    """

    __filters = {}

    def __init__(cls, name, bases, attrs) -> None:
        if "apply" not in attrs:
            raise AttributeError(f'class {cls} does not implement "apply(circuit)"')
        try:
            spec = inspect.getfullargspec(attrs["apply"])
            if not (
                spec.varargs is None
                and spec.varkw is None
                and spec.defaults is None
                and spec.args == ["self", "circuit"]
            ):
                raise TypeError
        except TypeError as e:
            raise AttributeError(f'class {cls} does not implement "apply(circuit)" properly') from e
        spec = inspect.getfullargspec(cls.__init__)
        if not (
            spec.varargs is None
            and spec.varkw is None
            and spec.defaults is None
            and spec.args == ["self", "recipe", "source", "target"]
        ):
            raise AttributeError(
                f"class {cls} does not implement " '"__init__(recipe, source, target)" properly'
            )
        type.__init__(cls, name, bases, attrs)
        if attrs.get("_visible", True):
            cls.__filters[name.replace("Filter", "")] = cls

    @classmethod
    def initialize(mcs, names, *args):
        """Create filters from a list of names.

        :param names: A list of filter class names to invoke
        :param args: Arguments to pass through to the filters
        :return: A list of filter instances
        """
        for fcls in mcs.__filters.values():
            if hasattr(fcls, "_checkpoint_name"):
                delattr(fcls, "_checkpoint_name")
        key = hashlib.sha256()
        key.update(b"foobar3000")
        filters = []
        for name in names:
            fcls = mcs.__filters.get(name, mcs.__filters.get(name + "Filter"))
            if fcls is None:
                raise ValueError(f"Cannot find filter '{name}'")
            key.update(fcls.__name__.encode())
            if hasattr(fcls, "_checkpoint_name"):
                raise ValueError(f"Cannot have more than one {fcls.__name__}")
            fcls._checkpoint_name = (
                f"{fcls.__name__.replace('Filter', '').lower()}" f"_{key.hexdigest()[:8]}"
            )
            try:
                filters.append(fcls(*args))
            except Exception as e:
                if fcls._required:
                    logger.fatal("Could not instantiate %s", fcls.__name__)
                    raise
                logger.warning("Disabling optional %s: %s", fcls.__name__, e)
        for i in range(len(filters) - 1, -1, -1):
            base = Path(checkpoint_resume.directory)
            parquet = filters[i]._checkpoint_name + ".parquet"
            table = filters[i]._checkpoint_name + ".ptable"
            fn = "_SUCCESS"
            if (base / parquet / fn).exists() or (base / table / fn).exists():
                classname = filters[i].__class__.__name__
                logger.info("Found checkpoint for %s", classname)
                break
        else:
            i = 0  # force initialization in case filters is empty
        for f in filters[:i]:
            classname = f.__class__.__name__
            logger.info("Removing %s", classname)
        return filters[i:]

    @classmethod
    def modules(mcs):
        """List registered subclasses."""
        return sorted(mcs.__filters.keys())


class DatasetOperation(metaclass=__DatasetOperationType):
    """Basis for synapse filters.

    Every filter should derive from :class:`~functionalizer.filters.DatasetOperation`,
    which will enforce the right format for the constructor
    and :meth:`~functionalizer.filters.DatasetOperation.apply` functions.
    The former is optional, but should be
    used to extract relevant information from the recipe.

    The two node populations are passed to the constructor to enable
    cross-checks between the recipe information and the population
    properties.  If the constructor raises an exception and the
    :attr:`._required` attribute is set to `False`, the filter will be
    skipped.

    If filters add or remove columns from the dataframe, this should be
    communicated via the :attr:`._columns` attribute, otherwise the general
    invocation of the filters will fail, as column consistency is checked.
    """

    _checkpoint = False
    """Store the results on disk, allows to skip computation on subsequent
    runs.
    """
    _checkpoint_buckets = None
    """Partition the data when checkpointing, avoids sort on load.
    """

    _visible = False
    """Determines the visibility of the filter to the user.
    """

    _reductive = True
    """Indicates if the filter is expected to reduce the touch count.
    """

    _required = True
    """If set to `False`, the filter will be skipped if recipe components
    are not found.
    """

    _columns = []
    """A list columns to be consumed and produced.

    Each item should be a tuple of two strings, giving the column
    consumed/dropped, and the column produced. If no column is dropped,
    `None` can be used. Likewise, if a column is only dropped, `None` can
    be the second element.

    Examples::

       (None, "synapse_id")  # will produce the column "synapse_id"
       ("synapse_id", None)  # will drop the colulmn "synapse_id"
       ("ham", "spam")       # will produce the colum "spam" while also
                             # dropping "ham". If the latter is not
                             # present, the former will not be
                             # added.
    """

    def __init__(self, recipe, source, target):
        """Empty constructor supposed to be overriden.

        Args:
            recipe: Wrapper around an XML document with parametrization information
            source: The source node population
            target: The target node population
        """

    def __call__(self, circuit):
        """Apply the operation to `circuit`."""
        classname = self.__class__.__name__
        logger.info("Applying %s", classname)
        with sm.jobgroup(classname):
            ran_filter = False  # assume loading from disk by default
            start = datetime.now()
            old_count = len(circuit)

            olds = set(circuit.df.columns)
            to_add = set(a for (c, a) in self._columns if not c or c in olds)
            to_drop = set(c for (c, _) in self._columns if c in olds)
            to_remove = olds & to_add

            if to_remove:
                logger.warning("Removing columns %s", ", ".join(to_remove))
                circuit.df = circuit.df.drop(*to_remove)
                olds -= to_remove

            if not self._checkpoint:
                ran_filter = True
                circuit.df = self.apply(circuit)
            else:

                @checkpoint_resume(
                    self._checkpoint_name,
                    bucket_cols=self._checkpoint_buckets,
                )
                def fun():
                    nonlocal ran_filter
                    ran_filter = True
                    return self.apply(circuit)

                circuit.df = fun()
            news = set(circuit.df.columns)

            dropped = olds - news
            added = news - olds

            if to_drop - dropped:
                raise RuntimeError(f"Undropped columns: {to_drop - dropped}")
            if dropped - to_drop:
                raise RuntimeError(f"Dropped columns: {dropped - to_drop}")
            if to_add - added:
                raise RuntimeError(f"Missing columns: {to_add - added}")
            if added - to_add:
                raise RuntimeError(f"Additional columns: {added - to_add}")

            if ran_filter:
                new_count = len(circuit)
                diff = old_count - new_count
                if self._reductive:
                    logger.info(  # pylint: disable=logging-fstring-interpolation
                        f"{classname} removed {diff:,d} touches, "
                        f"circuit now contains {new_count:,d}"
                    )
                elif diff != 0:
                    raise RuntimeError(f"{classname} removed touches, but should not")
                logger.info("%s application took %s", classname, datetime.now() - start)

            return circuit

    @abstractmethod
    def apply(self, circuit: Circuit):
        """Needs actual implementation of the operation.

        Takes a `Circuit`, applies some operations to it, and returns Spark dataframe
        representing the updated circuit.
        """

    @staticmethod
    def pathway_functions(columns, counts):
        """Construct pathway adding functions given columns and a value counts."""

        def _rename_maybe_numeric(col):
            if (col.startswith("src_") or col.startswith("dst_")) and not col.endswith("_i"):
                return f"{col}_i"
            return col

        def add_pathway(df):
            from pyspark.sql import functions as F

            pathway_column = F.lit(0)
            pathway_column_format = []
            pathway_column_values = []
            for col, factor in zip(columns, counts):
                name = _rename_maybe_numeric(col)
                pathway_column *= factor
                pathway_column += F.col(name)
                pathway_column_format.append(f"{name}(%d)")
                pathway_column_values.append(name)

            return df.withColumn("pathway_i", pathway_column).withColumn(
                "pathway_str",
                F.format_string(", ".join(pathway_column_format), *pathway_column_values),
            )

        return add_pathway
