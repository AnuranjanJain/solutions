# LeetCode Problem: Maximum Subarray
# URL: https://leetcode.com/problems/maximum-subarray/
# Day: 27
# Difficulty: Medium
# Date: 2025-05-26
# Status: Solved

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum