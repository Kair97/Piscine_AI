"""
This module provides basic statistical operations including mean, 
median, and population variance without using external libraries.
Author: kaorynbek
"""

def mean(values):
    return sum(values)/len(values)
def median(values):
    nums = sorted(values)
    n = len(nums)
    mid = n // 2
    if n % 2 != 0:
        return nums[mid]
    else:
        return (nums[mid - 1] + nums[mid]) / 2.0
def variance(values):
    m = mean(values)

    squared_deviations = [(x-m)**2 for x in values]

    return sum(squared_deviations) / len(values)