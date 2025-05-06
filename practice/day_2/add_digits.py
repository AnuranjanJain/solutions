# LeetCode Problem: Add Digits
# URL: https://leetcode.com/problems/add-digits/
# Day: 2
# Difficulty: Easy
# Date: 2025-05-01
# Status: Solved

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9
            