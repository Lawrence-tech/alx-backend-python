#!/usr/bin/env python3
"""
Write an async routine called wait_n that takes in 2 int arguments
(in this order) n and max_delay.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the specified
    max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for each wait_random
        call.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    # Create a list to store the tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Gather the tasks to run concurrently
    delays = await asyncio.gather(*tasks)

    # Sort the delays in ascending order
    delays.sort()

    return delays
