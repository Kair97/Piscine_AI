from __future__ import annotations

import numpy as np


def rotate_90(m: np.ndarray) -> np.ndarray:
    m = np.asarray(m)
    return np.rot90(m, k=-1).copy()


def transpose_no_T(m: np.ndarray) -> np.ndarray:
    m = np.asarray(m)
    return np.einsum("ij->ji", m)


def is_magic_square(m: np.ndarray) -> bool:
    m = np.asarray(m)
    if m.ndim != 2 or m.shape[0] != m.shape[1] or m.shape[0] == 0:
        return False

    row_sums = m.sum(axis=1)
    col_sums = m.sum(axis=0)
    main_diag = np.trace(m)
    anti_diag = np.trace(np.fliplr(m))

    magic_sum = row_sums[0]
    return bool(
        np.all(row_sums == magic_sum)
        and np.all(col_sums == magic_sum)
        and main_diag == magic_sum
        and anti_diag == magic_sum
    )


def block_trace(m: np.ndarray, k: int) -> np.ndarray:
    m = np.asarray(m)
    n = m.shape[0]
    if n == 0:
        return np.zeros((0, 0), dtype=m.dtype)

    reshaped = m.reshape(n // k, k, n // k, k)
    return np.einsum("acbc->ab", reshaped)


def top_k_indices(v: np.ndarray, k: int) -> np.ndarray:
    v = np.asarray(v)
    if k <= 0 or v.size == 0:
        return np.array([], dtype=int)

    k = min(k, v.size)
    idx = np.argpartition(v, -k)[-k:]
    return idx[np.argsort(-v[idx])]
