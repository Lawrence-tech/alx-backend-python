#!/usr/bin/env python3
"""
Module task_wait_n. task_wait_random is being called.
"""
import asyncio
from typing import List, Awaitable

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns task_wait_random n times with the specified max_delay

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds for each task_wait_random
        call.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    wait_times = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
            )
    return sorted(wait_times)
