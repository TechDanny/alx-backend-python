#!/usr/bin/env python3
"""
Tasks
"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    returns asyncio.Task
    """
    x = asyncio.get_event_loop()
    Task = x.create_task(wait_random(max_delay))
    return Task
