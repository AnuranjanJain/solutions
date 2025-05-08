# LeetCode Problem: Excel Sheet Column Number
# URL: https://leetcode.com/problems/excel-sheet-column-number/description/
# Day: 8
# Difficulty: Medium
# Date: 2025-05-07
# Status: Solved
# Solution for Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result