#!/usr/bin/env python3
"""
list of floats
"""


def sum_list(input_list: float) -> float:
    """
    returns the sum of list
    """
    total = 0
    for x in input_list:
        total += x
    return total
