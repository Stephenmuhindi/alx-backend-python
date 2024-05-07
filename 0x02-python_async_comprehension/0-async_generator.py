#!/usr/bin/env python3
"""
Async Generator
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loop 10 times,wait 1 second, yield a random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
