# LeetCode Problem: Happy Number
# URL: https://leetcode.com/problems/happy-number/description/
# Day: 6
# Difficulty: Medium
# Date: 2025-05-05
# Status: Solved
# Solution for Happy Number
# https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = sum(int(c)**2 for c in str(n))
            if n in seen:
                return False
            seen.add(n)
        return True
