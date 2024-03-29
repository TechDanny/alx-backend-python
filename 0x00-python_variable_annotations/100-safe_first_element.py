#!/usr/bin/env python3
"""
Duck typing
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    updated the function with the right annotation
    """
    if lst:
        return lst[0]
    else:
        return None
