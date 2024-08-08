#!/usr/bin/python3
"""Prime Game"""


def rm_multiples(n: int, nums: list) -> list:
    """Remove multiples"""
    for i in range(n * 2, len(nums), n):
        nums[i] = 0
    return nums


def isWinner(x: int, nums: list) -> str:
    """Prime Game"""
    if x == 0 or x == 1:
        return None
    if x != len(nums):
        return None
    if len(nums) == 0:
        return None
    nums[1] = 0
    for i in range(2, len(nums)):
        if nums[i] != 0:
            nums = rm_multiples(i, nums)
    if nums.count(0) >= x:
        return "Maria"
    return "Ben"
