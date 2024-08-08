#!/usr/bin/python3
"""Prime Game"""


def rm_multiples(x, nums):
    """Remove multiples"""
    for i in range(2, len(nums)):
        for j in range(i * 2, len(nums), i):
            if nums[j] % i == 0:
                nums[j] = 0
    return sorted(list(set(nums)))


def isWinner(x, nums):
    """Prime Game"""
    if x == 0 or x == 1:
        return None
    if x != len(nums):
        return None
    if len(nums) == 0:
        return None
    nums = rm_multiples(x, nums)
    if len(nums) % 2 == 0:
        return "Maria"
    return "Ben"
