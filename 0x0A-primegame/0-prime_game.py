#!/usr/bin/python3
"""Prime Game"""


def isPrime(n: int) -> bool:
    """Prime Game"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def rm_multiple(n: int, m: int) -> list:
    """Prime Game"""
    multiples = []
    for i in range(n, m + 1):
        if isPrime(i):
            multiples.append(i)
    return multiples


def isWinner(x: int, nums: list) -> str:
    """Prime Game"""
    if x == 0 or x == 1:
        return None
    if x != len(nums):
        return None
    
    maria = 0
    ben = 0
    multiples = rm_multiple(1, max(nums))
    for i in nums:
        if i in multiples:
            maria += 1
        else:
            ben += 1
    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
