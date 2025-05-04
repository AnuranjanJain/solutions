# LeetCode Problem: Missing Number
# URL: https://leetcode.com/problems/missing-number/
# Day: 1
# Difficulty: Easy
# Date: 2025-04-30
# Status: Solved

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        else:
            return i+1
