# LeetCode Problem: Valid Palindrome
# URL: https://leetcode.com/problems/valid-palindrome/description/
# Day: 38
# Difficulty: Easy
# Date: 2025-06-07
# Status: Solved

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))