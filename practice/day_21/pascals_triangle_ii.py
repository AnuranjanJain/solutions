# LeetCode Problem: Pascal's Triangle II
# URL: https://leetcode.com/problems/pascals-triangle-ii/
# Day: 21
# Difficulty: Easy
# Date: 2025-05-20
# Status: Solved

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]
        for i in range(1,rowIndex+1):
            ne=row[i-1]* (rowIndex-i+1)//i
            row.append(ne)
        return row