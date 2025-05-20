# LeetCode Problem: Valid Parenthesis String
# URL: https://leetcode.com/problems/valid-parenthesis-string/description/
# Day: 21
# Difficulty: Medium
# Date: 2025-05-20
# Status: Solved

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open, max_open = 0, 0 

        for ch in s:
            if ch == '(':
                min_open += 1
                max_open += 1
            elif ch == ')':
                min_open -= 1
                max_open -= 1
            else: 
                min_open -= 1  
                max_open += 1  
            
            if min_open < 0:  
                min_open = 0
            if max_open < 0: 
                return False

        return min_open == 0 
