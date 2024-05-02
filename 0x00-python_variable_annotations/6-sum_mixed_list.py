#!/usr/bin/env python3
"""
adds mixed list of integers and returns them as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum float"""
    return sum(mxd_lst)
