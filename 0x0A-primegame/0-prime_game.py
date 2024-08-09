#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """ Prime Game """
    if x == 0 or x == 1:
        return None
    if x != len(nums):
        return None
    n = max(nums)
    nums.sort()
    primes = [False for i in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if not primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = True
    primes[0] = primes[1] = True
    count = 0
    for i in range(len(primes)):
        if not primes[i]:
            count += 1
        primes[i] = count
    play = 0
    for n in nums:
        play += primes[n] % 2 == 1
    if play * 2 == len(nums):
        return None
    if play * 2 > len(nums):
        return "Maria"
    return "Ben"
