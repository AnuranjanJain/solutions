# LeetCode Problem: Palindrome Number
# URL: https://leetcode.com/problems/palindrome-number/
# Day: 4
# Difficulty: Easy
# Date: 2025-05-03
# Status: Solved
# Solution for Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        y=y[::-1]
        if str(x)==str(y):
            return True
        else:
            return False