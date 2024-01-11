#!/usr/bin/env python3
"""
Mixed list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    total = 0
    for x in mxd_lst:
        total += x
    return total
