# LeetCode Problem: Perfect Number
# URL: https://leetcode.com/problems/perfect-number/
# Day: 3
# Difficulty: Easy
# Date: 2025-05-02
# Status: Solved
# Solution for Perfect Number
# https://leetcode.com/problems/perfect-number/

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in {6, 28, 496, 8128, 33550336}