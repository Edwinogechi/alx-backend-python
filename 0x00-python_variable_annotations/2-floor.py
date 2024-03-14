#!/usr/bin/env python3
'''Task 2's module.
'''


def floor(n: float) -> int:
    '''Computes the floor of a floating-point number.

    Parameters:
        a (float): The floating-point number whose floor is to be computed.

    Returns:
        int: The floor of the input floating-point number.
    '''
    return int(n) if n >= 0 else int(n) - 1
