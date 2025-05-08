# LeetCode Problem: Nth Digit
# URL: https://leetcode.com/problems/nth-digit/description/
# Day: 9
# Difficulty: Medium
# Date: 2025-05-08
# Status: Solved

# Solution for Nth Digit
# https://leetcode.com/problems/nth-digit/description/

class Solution:
    def findNthDigit(self, n: int) -> int:
        length, count, start = 1, 9, 1

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        num = start + (n - 1) // length
        return int(str(num)[(n - 1) % length])
