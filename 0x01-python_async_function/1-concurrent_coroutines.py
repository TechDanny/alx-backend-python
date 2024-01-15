#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""


import asyncio
from typing import List

wait_random= __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns list of all delays
    """
    x = await asyncio.gather(*(wait_random(max_delay) for z in range(n)))
    return sorted(x)