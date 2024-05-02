#!/usr/bin/env python3
"""addition of a list of inputs"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    provides the sum of input
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
