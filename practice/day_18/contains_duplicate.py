# LeetCode Problem: Contains Duplicate
# URL: https://leetcode.com/problems/contains-duplicate
# Day: 18
# Difficulty: Easy
# Date: 2025-05-17
# Status: Solved

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False