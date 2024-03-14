#!/usr/bin/env python3
''' Description: Takes a list input_list of floats as argument and
    returns their sum as a float.
    Arguments: input_list: List[float]
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''computes sum of all elements in input_list. '''
    return float(sum(input_list))
