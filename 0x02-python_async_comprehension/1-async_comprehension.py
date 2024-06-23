#!/usr/bin/env python3
"""
    This module contains a coroutine called `async_comprehension`
    that returns a list of random numbers
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
        Asynchronous function that return a list of randorm numbers.
    '''
    return [i async for i in async_generator()]
