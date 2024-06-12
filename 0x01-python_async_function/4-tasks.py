#!/usr/bin/python3
'''task'''

import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_n(n: int, max_delay: int) -> List:
    return wait_n(n, max_delay)
