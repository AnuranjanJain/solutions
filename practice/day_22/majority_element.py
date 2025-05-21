# LeetCode Problem: Majority Element
# URL: https://leetcode.com/problems/majority-element/description/
# Day: 22
# Difficulty: Easy
# Date: 2025-05-21
# Status: Solved

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]