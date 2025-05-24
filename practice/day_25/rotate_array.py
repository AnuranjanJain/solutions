# LeetCode Problem: Rotate Array
# URL: https://leetcode.com/problems/rotate-array/submissions/1642885242/
# Day: 25
# Difficulty: Medium
# Date: 2025-05-24
# Status: Solved

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])