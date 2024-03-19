#!/usr/bin/env python3
''' Desription: Import async_comprehension from the previous file and write a
                measure_runtime coroutine that will execute async_comprehension
                four times in parallel using asyncio.gather.

                measure_runtime should measure the total runtime and return it.
                Notice that the total runtime is roughly 10 seconds, explain
                it to yourself.
'''

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Implements async_comprehension 4 times then measures the total
        implementation time in parallel. '''
    initial_time = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    following_time = time()

    return following_time - initial_time
