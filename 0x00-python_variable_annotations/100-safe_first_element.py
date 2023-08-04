#!/usr/bin/env python3
"""
Correct duck-typed annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Get the first element of the input list safely.

    Args:
        lst (Sequence[Any]): The list of elements.

    Returns:
        Union[Any, None]: The first element of the list if it exists, otherwise
        None.
    """
    if lst:
        return lst[0]
    else:
        return None
