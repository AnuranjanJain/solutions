# LeetCode Problem: Lexicographically Smallest Palindrome
# URL: https://leetcode.com/problems/lexicographically-smallest-palindrome/
# Day: 33
# Difficulty: Easy
# Date: 2025-06-01
# Status: Solved

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        a= len(s)-1
        b= 0
        s= list(s)
        while a>b:
            if s[a]<s[b]:
                s[b]=s[a]
            else:
                s[a]=s[b]
            a-=1
            b+=1
        return "".join([i for i in s])