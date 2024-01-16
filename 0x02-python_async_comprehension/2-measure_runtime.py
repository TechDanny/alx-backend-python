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
    start = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    stop = asyncio.get_event_loop().time()
    time_taken = stop - start
    return time_taken
