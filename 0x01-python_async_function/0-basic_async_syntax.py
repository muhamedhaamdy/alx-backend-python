#!/usr/bin/env python3
import asyncio
import random
'''async function'''


async def wait_random(max_delay: int = 10) -> float:
    '''sleep for a random time'''
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
