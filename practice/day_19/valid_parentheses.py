# LeetCode Problem: Valid Parentheses
# URL: https://leetcode.com/problems/valid-parentheses
# Day: 19
# Difficulty: Easy
# Date: 2025-05-18
# Status: Solved

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in hash:
                if stack and stack[-1] == hash[char]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(char)
        
        return not stack