#!/usr/bin/env python3 
'''multiple corotines'''

import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list:
    """Run wait_random n times and return a list of delays in ascending order."""
    delays = []
    
    async def insert_in_order(delay: float):
        """Insert delay in the correct position to keep the list sorted."""
        for i, current_delay in enumerate(delays):
            if delay < current_delay:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)
    
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        await insert_in_order(delay)
    
    return delays

