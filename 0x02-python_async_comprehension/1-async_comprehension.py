#!/usr/bin/env python3
import asyncio
import random
"""task 1"""


from .async_generator import async_generator

async def async_comprehension():
    return [i async for i in async_generator()]