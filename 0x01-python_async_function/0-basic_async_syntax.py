#!/usr/bin/env python3
""" Async basics  """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    The random module in Python provides
    functions for generating random numbers.
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
