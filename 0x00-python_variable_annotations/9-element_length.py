#!/usr/bin/env python3
''' Description: Annotate parameters and return values with appropriate types
    Parameters: data: Iterable[Sequence]
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''computes a list of tuples, each containing an element and its length.
    '''
    return [(i, len(i)) for i in lst]
