# LeetCode Problem: Longest Valid Parentheses
# URL: https://leetcode.com/problems/longest-valid-parentheses/description/
# Day: 23
# Difficulty: Hard
# Date: 2025-05-23
# Status: Solved

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Base index
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        
        return max_length