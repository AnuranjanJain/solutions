# LeetCode Problem: Longest Common Prefix
# URL: https://leetcode.com/problems/longest-common-prefix/
# Day: 41
# Difficulty: Easy
# Date: 2025-06-09
# Status: Solved

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        mn, mx = min(strs), max(strs)

        for i in range(len(mn)):
            if mn[i] != mx[i]: return mn[:i]
             
        return mn