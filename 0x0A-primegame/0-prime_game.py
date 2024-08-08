#!/usr/bin/python3
"""Prime Game"""


def rm_multiples(x, nums):
    """Remove multiples"""
    nums = sorted(nums)
    nums = list(dict.fromkeys(nums))
    nums = [num for num in nums if num % x != 0]
    return nums


def isWinner(x, nums):
    """Prime Game"""
    if not nums:
        return None

    if x != len(nums):
        return None

    if x == 0 or x == 1:
        return None

    if x % 2 == 0:
        return "Ben"
    nums = rm_multiples(2, nums)

    if not nums:
        return "Maria"
    return "Ben"
