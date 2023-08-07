#!/usr/bin/env python3
"""
measure_time function with integers n and max_delay as arguments that measures
the total execution time for wait_n(n, max_delay) and returns total_time / n.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay), and returns
    total_time / n.

    Args:
        n (int): The number of times to run wait_n.
        max_delay (int): The maximum delay in seconds for each wait_n call.

    Returns:
        float: The average execution time per wait_n call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    avg_time_per_call = total_time / n

    return avg_time_per_call
