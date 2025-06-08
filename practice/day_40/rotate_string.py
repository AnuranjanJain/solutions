# LeetCode Problem: Rotate String
# URL: https://leetcode.com/problems/rotate-string/
# Day: 40
# Difficulty: Easy
# Date: 2025-06-08
# Status: Solved

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        rs=[s[i:]+s[0:i] for i in range(len(s))]
        return goal in rs