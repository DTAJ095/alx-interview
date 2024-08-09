#!/usr/bin/python3
"""Prime Game"""


def rm_multiples(n: int, nums: list) -> list:
    """Remove multiples"""
    for i in range(2, len(nums)):
        if i * n < len(nums):
            nums[i * n] = 0
        else:
            break
    return nums


def isWinner(x: int, nums: list) -> str:
    """ Prime Game """
    if x == 0 or x == 1:
        return None
    if x != len(nums):
        return None

    maria = 0
    ben = 0

    primes = [1 for x in range(sorted(nums)[-1] + 1)]
    primes[0], primes[1] = 0, 0
    for i in range(2, len(primes)):
        a = rm_multiples(i, primes)

    for i in nums:
        if sum(primes[:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
