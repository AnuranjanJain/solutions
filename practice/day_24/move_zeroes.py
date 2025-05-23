# LeetCode Problem: Move Zeroes
# URL: https://leetcode.com/problems/move-zeroes/
# Day: 24
# Difficulty: Easy
# Date: 2025-05-23
# Status: Solved

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            if nums[i]==0:
                nums.append(0)
                nums.remove(0)