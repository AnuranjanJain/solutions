# LeetCode Problem: Greatest Common Divisor of Strings
# URL: https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Day: 45
# Difficulty: Easy
# Date: 2025-06-13
# Status: Solved

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1=len(str1)
        l2=len(str2)
        ans=gcd(l1,l2)
        return str1[:ans] if str1+str2==str2+str1 else ""o