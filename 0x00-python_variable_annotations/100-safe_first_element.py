#!/usr/bin/env python3
''' Description: Enhance the following code with the correct
                 duck-typed annotations
    Parameters: lst: Sequence[Any]
'''

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Returns the initial element of lst if it exists, otherwise None. '''
    if lst:
        return lst[0]
    else:
        return None
