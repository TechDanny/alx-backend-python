#!/usr/bin/env python3
"""
functions
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    calls another function
    """
    def another_multiplier(a: float) -> float:
        """
        returns a function that multiplies a float
        """
        return a * multiplier
    return another_multiplier
