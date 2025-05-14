# LeetCode Problem: Excel Sheet Column Title
# URL: https://leetcode.com/problems/excel-sheet-column-title/
# Day: 15
# Difficulty: Easy
# Date: 2025-05-14
# Status: Solved

class Solution:
    def solve(self, columnNumber):
        if columnNumber == 0:
            return ""
        columnNumber -= 1
        ans = chr(ord('A') + (columnNumber % 26))
        columnNumber //= 26
        return ans + self.solve(columnNumber)

    def convertToTitle(self, columnNumber):
        ans = self.solve(columnNumber)
        return ans[::-1] 

