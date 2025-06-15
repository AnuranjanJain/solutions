# LeetCode Problem: Number of 1 Bits
# URL: https://leetcode.com/problems/number-of-1-bits/description/
# Day: 47
# Difficulty: Easy
# Date: 2025-06-15
# Status: Solved

class Solution:
    def hammingWeight(self, n: int) -> int:
        no=list(bin(n))
        ans=0
        for i in no[2:]:
            if i=="1":
                ans+=1
        return ans