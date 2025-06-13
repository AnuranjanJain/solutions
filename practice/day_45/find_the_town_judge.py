# LeetCode Problem: Find the Town Judge
# URL: https://leetcode.com/problems/find-the-town-judge/description/
# Day: 45
# Difficulty: Easy
# Date: 2025-06-13
# Status: Solved

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        counts = [0] * (n + 1)
        for a, b in trust:
            counts[a] -= 1
            counts[b] += 1
        for i in range(1, n + 1):
            if counts[i] == n - 1:
                return i
        return -1