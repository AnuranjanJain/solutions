# LeetCode Problem: Length of Last Word
# URL: https://leetcode.com/problems/length-of-last-word/description/
# Day: 35
# Difficulty: Easy
# Date: 2025-06-02
# Status: Solved

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        s=s[::-1]
        c=0
        for i in s:
            if ord(i)!=32:
                c+=1
            else:
                return c
        return c