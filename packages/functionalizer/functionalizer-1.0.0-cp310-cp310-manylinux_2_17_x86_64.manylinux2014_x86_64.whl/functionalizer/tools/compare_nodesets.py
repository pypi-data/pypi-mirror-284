"""Compare two outputs of Spykfunc (coalesced), one filtered with NodeSets."""

import argparse
import sys

import libsonata
import numpy as np
import pyarrow.parquet as pq

from functionalizer.schema import LEGACY_MAPPING


def compare_nodesets():
    """Entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument("circuit", help="the circuit file with neuron definitions")
    parser.add_argument("full", help="the reference parquet file")
    parser.add_argument("filtered", help="the nodeset-filtered parquet file")
    parser.add_argument("region", type=int, help="Identifier of the target region")
    args = parser.parse_args()

    pop = libsonata.NodeStorage(args.circuit).open_population("All")
    regs = pop.get_enumeration("region", libsonata.Selection([[0, len(pop)]]))
    idx = np.argwhere(regs == args.region).flatten()

    df = pq.ParquetDataset(args.full).read().to_pandas().rename(columns=LEGACY_MAPPING)
    sel = df.target_node_id.isin(idx) & df.source_node_id.isin(idx)
    df_filtered = pq.ParquetDataset(args.filtered).read().to_pandas().rename(columns=LEGACY_MAPPING)

    if len(df[sel]) != len(df_filtered):
        print("\nDifferences in connections")
        print("==========================")
        print(f"Expected Dataframe Size: {len(df[sel]):10d}")
        print(f"Filtered Dataframe Size: {len(df_filtered):10d}")

        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    compare_nodesets()
