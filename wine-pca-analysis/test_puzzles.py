from __future__ import annotations

import numpy as np

from puzzles import (
    block_trace,
    is_magic_square,
    rotate_90,
    top_k_indices,
    transpose_no_T,
)


# ---------- rotate_90 ----------

def test_rotate_90_basic():
    m = np.array([[1, 2], [3, 4]])
    expected = np.array([[3, 1], [4, 2]])
    np.testing.assert_array_equal(rotate_90(m), expected)


def test_rotate_90_non_square():
    m = np.array([[1, 2, 3], [4, 5, 6]])
    expected = np.array([[4, 1], [5, 2], [6, 3]])
    np.testing.assert_array_equal(rotate_90(m), expected)


def test_rotate_90_single_element():
    m = np.array([[7]])
    np.testing.assert_array_equal(rotate_90(m), m)


def test_rotate_90_empty():
    m = np.empty((0, 0))
    assert rotate_90(m).shape == (0, 0)


# ---------- transpose_no_T ----------

def test_transpose_no_T_square():
    m = np.array([[1, 2], [3, 4]])
    expected = np.array([[1, 3], [2, 4]])
    np.testing.assert_array_equal(transpose_no_T(m), expected)


def test_transpose_no_T_rectangular():
    m = np.array([[1, 2, 3], [4, 5, 6]])
    expected = np.array([[1, 4], [2, 5], [3, 6]])
    np.testing.assert_array_equal(transpose_no_T(m), expected)


def test_transpose_no_T_matches_numpy():
    m = np.arange(12).reshape(3, 4)
    np.testing.assert_array_equal(transpose_no_T(m), m.T)


# ---------- is_magic_square ----------

def test_is_magic_square_true():
    m = np.array([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
    assert is_magic_square(m) is True


def test_is_magic_square_false_not_magic():
    m = np.array([[1, 2], [3, 4]])
    assert is_magic_square(m) is False


def test_is_magic_square_non_square_returns_false():
    m = np.array([[1, 2, 3], [4, 5, 6]])
    assert is_magic_square(m) is False


def test_is_magic_square_non_2d_returns_false():
    m = np.array([1, 2, 3])
    assert is_magic_square(m) is False


# ---------- block_trace ----------

def test_block_trace_spec_example():
    m = np.arange(16).reshape(4, 4)
    expected = np.array([[5, 9], [21, 25]])
    np.testing.assert_array_equal(block_trace(m, 2), expected)


def test_block_trace_k_equals_1():
    m = np.array([[1, 2], [3, 4]])
    # каждый блок 1x1, след блока = сам элемент
    np.testing.assert_array_equal(block_trace(m, 1), m)


def test_block_trace_k_equals_n():
    m = np.arange(9).reshape(3, 3)
    # один блок размером с саму матрицу
    expected = np.array([[np.trace(m)]])
    np.testing.assert_array_equal(block_trace(m, 3), expected)


# ---------- top_k_indices ----------

def test_top_k_indices_basic():
    v = np.array([3, 1, 4, 1, 5, 9, 2, 6])
    result = top_k_indices(v, 3)
    np.testing.assert_array_equal(result, np.array([5, 7, 4]))


def test_top_k_indices_k_zero():
    v = np.array([1, 2, 3])
    result = top_k_indices(v, 0)
    assert result.size == 0


def test_top_k_indices_k_larger_than_length():
    v = np.array([10, 20, 30])
    result = top_k_indices(v, 10)
    np.testing.assert_array_equal(result, np.array([2, 1, 0]))