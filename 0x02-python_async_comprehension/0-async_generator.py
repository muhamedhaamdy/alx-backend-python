#!/usr/bin/env python3
"""
    This module contains a coroutine called `async_generator`
    that generates random numbers
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers between 1 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
