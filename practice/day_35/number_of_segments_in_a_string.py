# LeetCode Problem: Number of Segments in a String
# URL: https://leetcode.com/problems/number-of-segments-in-a-string/description/
# Day: 35
# Difficulty: Easy
# Date: 2025-06-03
# Status: Solved

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split()) 