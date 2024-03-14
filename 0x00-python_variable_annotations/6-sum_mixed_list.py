#!/usr/bin/env python3
''' Description: Takes given list mxd_lst of floats and integers then
    returns their sum as a float.
    Parameters: mxd_lst: List[Union[int, float]]
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Outputs sum of elements of mxd_list. '''
    return float(sum(mxd_lst))