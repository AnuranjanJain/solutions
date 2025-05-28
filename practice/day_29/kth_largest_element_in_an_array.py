# LeetCode Problem: Kth Largest Element in an Array
# URL: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Day: 29
# Difficulty: Medium
# Date: 2025-05-28
# Status: Solved

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]