#!/usr/bin/env python3
''' Defines a function task_wait_random that accepts an integer max_delay
    as an argument and returns an asyncio.Task object.
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    ''' Returns an asyncio.Task object for waiting for a random delay. '''
    return asyncio.create_task(wait_random(max_delay))
