# LeetCode Problem: Count Primes
# URL: https://leetcode.com/problems/count-primes/
# Day: 49
# Difficulty: Medium
# Date: 2025-06-18
# Status: Solved

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        p = 2
        while p * p < n:
            if isPrime[p]:
                for multiple in range(p * p, n, p):
                    isPrime[multiple] = False
            p += 1
        return sum(isPrime)