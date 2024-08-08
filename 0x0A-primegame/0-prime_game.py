#!/usr/bin/python3
"""Prime Game"""


# def rm_multiples(n: int, nums: list) -> list:
#     """Remove multiples"""
#     for i in range(2, len(nums)):
#         if i * n < len(nums):
#             nums[i * n] = 0
#         else:
#             break
#     return nums


# def isWinner(x: int, nums: list) -> str:
#     """ Prime Game """
#     if x == 0 or x == 1:
#         return None
#     if x != len(nums):
#         return None

#     maria = 0
#     ben = 0

#     primes = [1 for x in range(sorted(nums)[-1] + 1)]
#     primes[0], primes[1] = 0, 0
#     for i in range(2, len(primes)):
#         a = rm_multiples(i, primes)

#     for i in nums:
#         if sum(primes[:i + 1]) % 2 == 0:
#             ben += 1
#         else:
#             maria += 1
#     if maria > ben:
#         return "Maria"
#     if ben > maria:
#         return "Ben"
#     return None
def isWinner(x, nums):
    """ Prime Game """
    if not nums or x < 1:
        return None
    n = max(nums)
    nums.sort()
    m = [False for i in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if not m[i]:
            for j in range(i*i, n + 1, i):
                m[j] = True
    m[0] = m[1] = True
    c = 0
    for i in range(len(m)):
        if not m[i]:
            c += 1
        m[i] = c
    p1 = 0
    for n in nums:
        p1 += m[n] % 2 == 1
    if p1 * 2 == len(nums):
        return None
    if p1 * 2 > len(nums):
        return "Maria"
    return "Ben"