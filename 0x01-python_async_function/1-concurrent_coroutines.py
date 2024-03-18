#!/usr/bin/env python3
''' Imports wait_random from a previous Python file and defines an asynchronous
    routine called wait_n. wait_n takes two integer arguments: max_delay and n.
    It spawns wait_random n times with the specified max_delay.

    wait_n returns a list containing all the delays (float values). The delays
    in the list are sorted in ascending order without using the sort() function
    due to concurrency considerations.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.
    '''
    delay_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(delay_times)
