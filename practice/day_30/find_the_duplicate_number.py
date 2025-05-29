# LeetCode Problem: Find the Duplicate Number
# URL: https://leetcode.com/problems/find-the-duplicate-number/description/
# Day: 30
# Difficulty: Medium
# Date: 2025-05-29
# Status: Solved

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ind = abs(nums[i])
            if nums[ind] < 0:
                return ind
            nums[ind] = -nums[ind]
        return -1