#!/usr/bin/env python3
"""
Measure the runtime
"""


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns total_time / n
    """
    begin = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop = time.time()
    total_time = stop - begin

    return total_time / n
