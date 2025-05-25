# LeetCode Problem: Find First and Last Position of Element in Sorted Array
# URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Day: 26
# Difficulty: Medium
# Date: 2025-05-25
# Status: Solved

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]