#!/usr/bin/env python3
"""
Annotate function's parameters and return values
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Get the length of elements in the input list.

    Args:
        lst (Iterable[Sequence]): The list of elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing an
        element from lst and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
