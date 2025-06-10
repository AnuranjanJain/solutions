# LeetCode Problem: Reverse Words in a String
# URL: https://leetcode.com/problems/reverse-words-in-a-string/
# Day: 42
# Difficulty: Medium
# Date: 2025-06-10
# Status: Solved

class Solution:
    def reverseWords(self, s: str) -> str:
        val=list(s.split())
        return " ".join(val[::-1])