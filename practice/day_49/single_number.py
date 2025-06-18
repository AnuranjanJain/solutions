# LeetCode Problem: Single Number
# URL: https://leetcode.com/problems/single-number/description/
# Day: 49
# Difficulty: Easy
# Date: 2025-06-18
# Status: Solved

class Solution:
    def singleNumber(self, nums: List[int]):
        r=0
        for i in nums:
            r=r^i 
        return r