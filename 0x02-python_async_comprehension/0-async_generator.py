#!/usr/bin/env python3
"""
Async_generator that takes no arguments
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    This coroutine loops 10 times, waiting asynchronously for 1 second in each
    iteration and then yielding a random floating-point number between 0 and 10
    using the random.uniform function.

    Yields:
        float: A random number between 0 and 10.

    Examples:
        >>> async def print_yielded_values():
        ...     result = []
        ...     async for i in async_generator():
        ...         result.append(i)
        ...     print(result)
        ...
        >>> asyncio.run(print_yielded_values())
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
