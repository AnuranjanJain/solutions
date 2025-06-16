# LeetCode Problem: Check If It Is a Good Array
# URL: https://leetcode.com/problems/check-if-it-is-a-good-array/
# Day: 48
# Difficulty: Hard
# Date: 2025-06-16
# Status: Solved

from math import gcd
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        x = 0
        for num in nums:
            x = gcd(x, num)
        return True if x == 1 else False