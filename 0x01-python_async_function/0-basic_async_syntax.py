#!/usr/bin/env python3
"""
asynchronous coroutine that takes in an integer argument (max_delay, with a
default value of 10) named wait_random that waits for a random delay between
0 and max_delay (included and float value) seconds and eventually returns it.
"""
import asyncio
import random


# Define an asynchronous coroutine called wait_random
async def wait_random(max_delay=10):
    # Generate a random float value between 0 and max_delay
    delay = random.uniform(0, max_delay)

    # Suspend the coroutine's execution for the generated delay
    await asyncio.sleep(delay)

    # Return the actual delay that was used
    return delay


# Define another asynchronous coroutine to demonstrate calling wait_random
async def main():
    # Call wait_random with default max_delay and await the result
    result = await wait_random()
    print(f"Waited for {result:.2f} seconds")

# Assuming you're running this inside an asyncio event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
