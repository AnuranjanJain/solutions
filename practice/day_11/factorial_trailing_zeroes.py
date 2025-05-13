

# LeetCode Problem: Factorial Trailing Zeroes
# URL: https://leetcode.com/problems/factorial-trailing-zeroes/description/
# Day: 11
# Difficulty: Medium
# Date: 2025-05-10
# Status: Solved
# Solution for Factorial Trailing Zeroes


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count