#!/usr/bin/env python3

"""
Type checking
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """
    Zooms in on the elements of a given list by repeating each element multiple
    times.

    This function takes a tuple 'lst' and an optional integer 'factor'.
    It creates a new list where each element from 'lst' is repeated 'factor'
    times.

    Parameters:
        lst (Tuple[int]): The input tuple containing elements to be zoomed in.
        factor (int, optional): The factor by which each element should be
        repeated. Defaults to 2.

    Returns:
        List[int]: A new list containing elements from 'lst' repeated 'factor'
        times.

    Example:
        >>> array = (12, 72, 91)
        >>> zoom_2x = zoom_array(array)
        >>> print(zoom_2x)
        [12, 12, 72, 72, 91, 91]

        >>> zoom_3x = zoom_array(array, 3)
        >>> print(zoom_3x)
        [12, 12, 12, 72, 72, 72, 91, 91, 91]
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


# Example usage:
array = (12, 72, 91)

# Zoom the array by a factor of 2 (default)
zoom_2x = zoom_array(array)

# Zoom the array by a factor of 3
zoom_3x = zoom_array(array, 3)
