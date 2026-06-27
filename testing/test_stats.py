import pytest
from stats import mean, median, variance, mode 

def test_variance_basic():
    assert variance([2, 4, 4, 4, 5, 5, 7, 9]) == 4.0

def test_mean_sample_data(sample_data):
    assert(mean(sample_data)) == 18.0

def test_median_sample_data(sample_data):
    assert(median(sample_data)) == 15.5


@pytest.mark.parametrize("values,expected", [
    ([1, 2, 3, 4, 5], 3.0),
    ([42],            42.0),
    ([0, 0, 0],       0.0),
    ([-1, 0, 1],      0.0),
    ([10],            10.0),
])
def test_mean(values, expected):
    assert mean(values) == expected

@pytest.mark.parametrize("values,expected", [
    ([1, 2, 3], 2.0),
    ([-1, 0, 1, 5], 0.5),
    ([42], 42.0),
    ([10, 20, 30], 20.0),
])

def test_median(values, expected):
    assert median(values) == expected

def test_mean_empty_raises(empty_list):
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        mean(empty_list)

def test_median_empty_raises(empty_list):
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        median(empty_list)

def test_variance_empty_raises(empty_list):
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        variance(empty_list)

def test_mode_single_mode():
    assert mode([1, 2, 2, 2, 3]) == 2

def test_mode_tie_break():
    assert mode([1, 1, 2, 2, 3]) == 1

def test_mode_single_element():
    assert mode([42]) == 42

def test_mode_empty_raises():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        mode([])