#!/usr/bin/env python3
"""
asynchronous coroutine that takes in an integer argument (max_delay, with a
default value of 10) named wait_random that waits for a random delay between
0 and max_delay (included and float value) seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay seconds.

    Args:
        max_delay (int, optional): The maximum delay in seconds. Defaults
        to 10.

    Returns:
        float: The actual delay that was used.
    """
    # Generate a random float value between 0 and max_delay
    delay = random.uniform(0, max_delay)

    # Suspend the coroutine's execution for the generated delay
    await asyncio.sleep(delay)

    # Return the actual delay that was used
    return delay
