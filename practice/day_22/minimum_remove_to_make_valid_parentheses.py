# LeetCode Problem: Minimum Remove to Make Valid Parentheses
# URL: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
# Day: 22
# Difficulty: Medium
# Date: 2025-05-21
# Status: Solved

class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''  # remove unmatched ')'

        while stack:
            s[stack.pop()] = ''  # remove unmatched '('

        return ''.join(s)