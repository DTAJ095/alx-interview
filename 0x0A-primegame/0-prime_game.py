#!/usr/bin/python3
"""Prime Game"""


def rm_multipes(n: int, ls: list) -> list:
    """Remove multiples"""
    for i in range(2, n + 1):
        if ls[i] == 0:
            continue
        for j in range(i * i, n + 1, i):
            ls[j] = 0
    return ls

def isWinner(x: int, nums: list) -> str:
    """Prime Game"""
    if x == 0 or x == 1:
        return None
    ls = [1] * (max(nums) + 1)
    ls = rm_multipes(max(nums), ls)
    prime = 0
    for i in range(2, len(ls)):
        if ls[i] == 1:
            prime += 1
        ls[i] = prime
    if prime % 2 == 0:
        return "Maria"
    return "Ben"
