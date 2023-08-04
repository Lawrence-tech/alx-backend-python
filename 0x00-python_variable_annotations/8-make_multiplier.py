#!/usr/bin/env python3
"""
Type annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function based on the given multiplier.

    Args:
        multiplier (float): The float multiplier.

    Returns:
        Callable[[float], float]: A function that takes a float argument and
        returns the product of the float and multiplier.
    """
    def multiplier_function(num: float) -> float:
        return num * multiplier

    return multiplier_function
