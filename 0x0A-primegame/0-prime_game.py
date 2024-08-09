#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """ Prime Game """
    if not nums or x < 1:
        return None
    n = max(nums)
    nums.sort()
    primes = [False for i in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if not primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = True
    primes[0] = primes[1] = True
    c = 0
    for i in range(len(primes)):
        if not primes[i]:
            c += 1
        primes[i] = c
    p1 = 0
    for k in nums:
        p1 += primes[k] % 2 == 1
    if p1 * 2 == len(nums):
        return None
    if p1 * 2 > len(nums):
        return "Maria"
    return "Ben"
