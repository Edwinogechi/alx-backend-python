#!/usr/bin/env python3
''' Asynchronous coroutine that accepts an integer argument named max_delay
    (default value: 10). It waits for a random delay between 0 and max_delay
    (inclusive, float value) seconds and eventually returns it.
    Arguments:
        max_delay (int): The maximum delay time (default: 10).
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Waits for delay up to max_delay seconds and returns the delay. '''
    time_taken = max_delay * random.random()
    await asyncio.sleep(time_taken)
    return time_taken
