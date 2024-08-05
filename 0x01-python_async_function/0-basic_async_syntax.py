#!/usr/bin/env python3
"""Basic async syntax"""


import asyncio
import random


# Definition of function
async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits
    for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay that the coroutine waited.
    """
    # Generate a random delay between 0 and max_delay seconds
    delay = random.uniform(0, max_delay)

    # Awaiting for the random delay using sleep functionality
    await asyncio.sleep(delay)

    return delay
