# LeetCode Problem: Search Insert Position
# URL: https://leetcode.com/problems/search-insert-position/description/
# Day: 23
# Difficulty: Easy
# Date: 2025-05-23
# Status: Solved

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return start