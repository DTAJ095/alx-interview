#!/usr/bin/python3
"""Prime Game"""


def isPrime(n: int) -> bool:
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def rm_multiples(n: int, primes: list) -> list:
    """Remove multiples of a number"""
    for i in range(2 * n, len(primes), n):
        primes[i] = 0
    return primes


def isWinner(x: int, nums: list) -> str:
    """ Prime Game """
    if x == 0 or x == 1:
        return None
    if x != len(nums):
        return None

    maria = 0
    ben = 0
    primes = [0, 0] + [1] * (max(nums) - 1)
    for i in range(2, len(primes)):
        if primes[i] == 1:
            primes = rm_multiples(i, primes)
    for n in nums:
        if primes[n]:
            maria += 1
        else:
            ben += 1
    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
