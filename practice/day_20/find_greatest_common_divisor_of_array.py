# LeetCode Problem: Find Greatest Common Divisor of Array
# URL: https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
# Day: 20
# Difficulty: Easy
# Date: 2025-05-19
# Status: Solved

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smol=min(nums)
        big=max(nums)
        return math.gcd(smol,big)