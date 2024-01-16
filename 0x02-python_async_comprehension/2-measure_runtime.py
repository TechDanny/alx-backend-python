#!/usr/bin/env python3
"""
 Run time for four parallel comprehensions
"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures the total runtime and returns it
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    stop = time.perf_counter()
    time_taken = stop - start
    return time_taken
