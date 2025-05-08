# LeetCode Problem: Valid Perfect Square
# URL: https://leetcode.com/problems/valid-perfect-square/
# Day: 5
# Difficulty: Easy
# Date: 2025-05-04
# Status: Solved
# Solution for Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num**0.5)==int(num**0.5):
            return True
        else:
            return False