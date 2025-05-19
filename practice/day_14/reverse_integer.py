# LeetCode Problem: Reverse Integer
# URL: https://leetcode.com/problems/reverse-integer/submissions/1633029772/
# Day: 14
# Difficulty: Medium
# Date: 2025-05-13
# Status: Solved

class Solution:
    def reverse(self, x: int) -> int:
        
        rev=(str(abs(x)))[::-1]
        if int(rev)>((2**31)-1) or -1*int(rev)<-(2**31):
            return 0
        else:
            return int(rev) if x>0 else -1*int(rev)