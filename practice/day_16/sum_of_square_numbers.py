# LeetCode Problem: Sum of Square Numbers
# URL: https://leetcode.com/problems/sum-of-square-numbers
# Day: 16
# Difficulty: Medium
# Date: 2025-05-15
# Status: Solved

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = (c - a * a) ** 0.5
            if b == int(b):
                return True
            a += 1
        return False