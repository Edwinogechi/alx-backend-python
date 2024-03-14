#!/usr/bin/env python3
'''
    Brief: Use type annotations based on its parameters and return values.
    Parameters: T - a TypeVar with value '~T'
'''

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    ''' Outputs value of dct[key] if present; otherwise, returns `default`. '''
    if key in dct:
        return dct[key]
    else:
        return default
