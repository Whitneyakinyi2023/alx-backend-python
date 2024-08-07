#!/usr/bin/env python3
import asyncio
import random
"""generator"""


async def async_generator():
    """Function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
