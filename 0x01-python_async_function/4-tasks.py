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
    # Create a list to store the tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Gather the tasks to run concurrently
    delays = await asyncio.gather(*tasks)

    # Sort the delays in ascending order
    delays.sort()

    return delays
