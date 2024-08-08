#!/usr/bin/python3
"""Prime Game"""
from typing import List


def isWinner(x: int, nums: List[int]) -> str:
    """Prime Game"""
    if x == 0 or x == 1:
        return None
    if x % 2 == 0:
        return "Ben"
    return "Maria"
