# LeetCode Problem: Count Odd Numbers In An Interval Range
# URL: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
# Day: 12
# Difficulty: Medium
# Date: 2025-05-11
# Status: Solved
# Solution for Count Odd Numbers In An Interval Range
# 

# Solution for Count Odd Numbers in an Interval Range
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)