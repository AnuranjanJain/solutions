# LeetCode Problem: Break a Palindrome
# URL: https://leetcode.com/problems/break-a-palindrome
# Day: 50
# Difficulty: Medium
# Date: 2025-06-18
# Status: Solved

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palindrome = list(palindrome)
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
        palindrome[-1] = 'b'
        return ''.join(palindrome)