#!/usr/bin/env python3
''' Defines a measure_time function that takes integers n and max_delay
    as arguments. It measures the total execution time for wait_n(n, max_delay)
    and returns the average time taken per iteration (total_time / n).
    The function returns a float value.
'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Measures the average execution time per iteration for wait_n. '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
