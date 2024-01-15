#!/usr/bin/env python3
"""
Tasks
"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """

    """
    x = [task_wait_random(max_delay) for _ in range(n)]
    await asyncio.gather(*x)
    delays = [task.result() for task in x]
    return sorted(delays)
