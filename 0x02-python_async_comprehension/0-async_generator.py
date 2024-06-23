#!/usr/bin/env python3
import asyncio
import random

"""
    This module contains a coroutine called `async_generator` that generates random numbers
"""


async def async_generator():
    """
    Asynchronous generator that yields random numbers between 1 and 10.

    This generator uses the `asyncio.sleep()` function to introduce a delay of 1 second
    between each yield statement. It generates a total of 10 random numbers.

    Yields:
        float: A random number between 1 and 10.

    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
