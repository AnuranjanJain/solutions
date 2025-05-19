# LeetCode Problem: Two Sum
# URL: https://leetcode.com/problems/two-sum
# Day: 17
# Difficulty: Easy
# Date: 2025-05-16
# Status: Solved

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return []