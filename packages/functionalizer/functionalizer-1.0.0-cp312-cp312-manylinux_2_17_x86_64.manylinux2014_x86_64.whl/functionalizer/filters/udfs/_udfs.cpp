#include <random>

#include <Random123/threefry.h>

#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;
using namespace py::literals;


namespace {

class RNG {
  public:
    using result_type = size_t;

    RNG(size_t seed, size_t key, size_t derivate)
    : key_{seed, seed, key, derivate} {
    };

    inline result_type operator()() {
        if (index_ == 0) {
            for (size_t i = 0; i < counter_.size(); ++i) {
                if (counter_[i] == max()) {
                    counter_[i] = 0;
                } else {
                    counter_[i] += 1;
                    break;
                }
            }
            index_ = counter_.size();
            values_ = rng_(counter_, key_);
        }
        return values_[--index_];
    };

    result_type max() const {
        return std::numeric_limits<result_type>::max();
    }

    result_type min() const {
        return std::numeric_limits<result_type>::min();
    }

  private:
    r123::Threefry4x64 rng_ = {};
    r123::Threefry4x64::ctr_type counter_ = {{}};
    r123::Threefry4x64::key_type key_ = {{}};
    r123::Threefry4x64::ctr_type values_ = {{}};
    size_t index_ = 0;
};

}  // namespace


namespace std {

template <>
struct hash<std::pair<int, int>> {
    size_t operator()(const std::pair<int, int>& k) const {
        static_assert(sizeof(size_t) == 2 * sizeof(int));
        return hash<size_t>()((static_cast<size_t>(k.first) << sizeof(int)) |
                              static_cast<size_t>(k.second));
    }
};

}  // namespace std


namespace fz {

namespace junctions {

using indices = std::pair<std::vector<size_t>, std::vector<size_t>>;
using key = std::pair<int, int>;
using index_map = std::unordered_map<key, indices>;

/// Return the indices of two unique ids in src
///
/// \param src primary list of ids to index
/// \param dst secondary list of ids to cross-check
/// \throws std::runtime_error if more than two unique ids are present in src, dst
/// \returns a std::pair of indices for the two unique ids
index_map _indices(const py::array_t<int>& src, const py::array_t<int>& dst) {
    index_map result;

    const auto _src = src.data(0);
    const auto _dst = dst.data(0);

    for (size_t i = 0; i < src.shape(0); ++i) {
        if (_src[i] == _dst[i]) {
            continue;
        } else if (_src[i] > _dst[i]) {
            result[std::make_pair(_dst[i], _src[i])].second.push_back(i);
        } else {
            result[std::make_pair(_src[i], _dst[i])].first.push_back(i);
        }
    }

    return result;
}


py::array_t<unsigned char> match_dendrites(const py::array_t<int>& src,
                                           const py::array_t<int>& dst,
                                           py::array_t<unsigned char>& pre_sec,
                                           py::array_t<unsigned char>& pre_seg,
                                           const py::array_t<long>& pre_jct,
                                           py::array_t<unsigned char>& post_sec,
                                           py::array_t<unsigned char>& post_seg,
                                           py::array_t<long>& post_jct) {
    py::array_t<int> accept(src.shape(0));

    if (src.shape(0) == 0) {
        return accept;
    }

    auto _res = accept.mutable_data(0);
    for (size_t i = 0; i < accept.shape(0); ++i) {
        _res[i] = 0;
    }

    auto idxs = _indices(src, dst);

    auto _pre_sec = pre_sec.mutable_data(0);
    auto _pre_seg = pre_seg.mutable_data(0);
    auto _pre_jct = pre_jct.data(0);

    auto _post_sec = post_sec.mutable_data(0);
    auto _post_seg = post_seg.mutable_data(0);
    auto _post_jct = post_jct.mutable_data(0);

    auto match = [&](size_t i, std::vector<size_t> js) -> long {
        long fuzzy = -1;
        for (const auto j: js) {
            if (_res[j] > 0) {
                // skip already accepted connections
                continue;
            } else if (_pre_sec[i] == _post_sec[j] and _pre_sec[j] == _post_sec[i]) {
                const auto diff_ij = std::abs(_pre_seg[i] - _post_seg[j]);
                const auto diff_ji = std::abs(_pre_seg[j] - _post_seg[i]);
                if (diff_ij == 0 and diff_ji == 0) {
                    return j;
                } else if (diff_ij <= 1 and diff_ji <= 1 and fuzzy < 0) {
                    fuzzy = j;
                }
            }
        }
        return fuzzy;
    };

    for (const auto& p: idxs) {
        const auto& is = p.second.first;
        const auto& js = p.second.second;
        for (const auto i: is) {
            const auto j = match(i, js);

            if (j >= 0) {
                _res[i] = 1;
                _res[j] = 1;
                _pre_sec[i] = _post_sec[j];
                _pre_seg[i] = _post_seg[j];
                _post_sec[i] = _pre_sec[j];
                _post_seg[i] = _pre_seg[j];
                _post_jct[i] = _pre_jct[j];
                _post_jct[j] = _pre_jct[i];
            }
        }
    }

    return accept;
}

}  // namespace junctions

namespace random {

py::array_t<float> uniform(int seed, int key, py::array_t<long> subkey) {
    py::array_t<float> result(subkey.shape(0));

    auto _result = result.mutable_data(0);
    auto _subkey = subkey.data(0);

    std::uniform_real_distribution<float> dist(0., 1.);
    for (size_t i = 0; i < result.shape(0); ++i) {
        RNG rng(seed, key, _subkey[i]);
        _result[i] = dist(rng);
    }
    return result;
}


py::array_t<int> poisson(int seed, int key, py::array_t<long> subkey, py::array_t<float> k) {
    py::array_t<int> result(subkey.shape(0));

    auto _result = result.mutable_data(0);
    auto _subkey = subkey.data(0);
    auto _k = k.data(0);

    for (size_t i = 0; i < result.shape(0); ++i) {
        if (_k[i] >= 1.) {
            std::poisson_distribution<> dist(_k[i] - 1);
            RNG rng(seed, key, _subkey[i]);
            _result[i] = 1 + dist(rng);
        } else {
            _result[i] = 1;
        }
    }
    return result;
}


py::array_t<float> gamma(int seed,
                         int key,
                         py::array_t<long> subkey,
                         py::array_t<float> m,
                         py::array_t<float> sd) {
    py::array_t<float> result(subkey.shape(0));

    auto _result = result.mutable_data(0);
    auto _subkey = subkey.data(0);

    auto _m = m.data(0);
    auto _sd = sd.data(0);

    for (size_t i = 0; i < result.shape(0); ++i) {
        const double _mi = _m[i];
        const double _sdi = _sd[i];
        const double shape = _mi * _mi / (_sdi * _sdi);
        const double scale = _sdi * _sdi / _mi;

        std::gamma_distribution<float> dist(shape, scale);
        RNG rng(seed, key, _subkey[i]);
        _result[i] = dist(rng);
    }

    return result;
}


py::array_t<float> truncated_normal(int seed,
                                    int key,
                                    py::array_t<long> subkey,
                                    py::array_t<float> m,
                                    py::array_t<float> sd) {
    py::array_t<float> result(subkey.shape(0));

    auto _result = result.mutable_data(0);
    auto _subkey = subkey.data(0);

    auto _m = m.data(0);
    auto _sd = sd.data(0);

    for (size_t i = 0; i < result.shape(0); ++i) {
        std::normal_distribution<> dist(0.f, 1.f);
        RNG rng(seed, key, _subkey[i]);
        do {
            float num;
            do {
                num = dist(rng);
            } while (std::abs(num) > 1.f);
            _result[i] = _sd[i] * num + _m[i];
        } while (_result[i] < 0);
    }

    return result;
}

}  // namespace random


py::array_t<int> get_bins(const py::array_t<float>& target, const py::array_t<float>& boundaries) {
    py::array_t<int> result(target.shape(0));

    const auto xs = target.data(0);
    const auto bins = boundaries.data(0);
    auto res = result.mutable_data(0);

    for (size_t i = 0; i < target.shape(0); ++i) {
        res[i] = -1;
        for (size_t j = boundaries.shape(0); j > 0; --j) {
            if (xs[i] >= bins[j - 1]) {
                res[i] = j - 1;
                break;
            }
        }
    }
    return result;
}

}  // namespace fz

PYBIND11_MODULE(_udfs, m) {
    m.doc() = "Accelerated functions for Apache Spark UDFs";

    m.def("uniform", &fz::random::uniform, "seed"_a, "key"_a, "subkey"_a);
    m.def("poisson", &fz::random::poisson, "seed"_a, "key"_a, "subkey"_a, "k"_a);
    m.def("gamma", &fz::random::gamma, "seed"_a, "key"_a, "subkey"_a, "m"_a, "sd"_a);
    m.def("truncated_normal",
          &fz::random::truncated_normal,
          "seed"_a,
          "key"_a,
          "subkey"_a,
          "m"_a,
          "sd"_a);

    m.def("get_bins", &fz::get_bins, "target"_a, "boundaries"_a);

    m.def("match_dendrites",
          &fz::junctions::match_dendrites,
          "src"_a,
          "dst"_a,
          "pre_sec"_a,
          "pre_seg"_a,
          "pre_jct"_a,
          "post_sec"_a,
          "post_seg"_a,
          "post_jct"_a);
}
