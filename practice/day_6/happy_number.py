# LeetCode Problem: Happy Number
# URL: 
# Day: 6
# Difficulty: Medium
# Date: 2025-05-05
# Status: Solved

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = sum(int(c)**2 for c in str(n))
            if n in seen:
                return False
            seen.add(n)
        return True
