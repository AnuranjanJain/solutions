# LeetCode Problem: Evaluate Reverse Polish Notation
# URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# Day: 20
# Difficulty: Medium
# Date: 2025-05-19
# Status: Solved

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid=['+','-','*','/']
        stack=[]
        for t in tokens:
            if t in valid:
                val1=stack.pop()
                val2=stack.pop()
                if t == '+':
                    stack.append(val1+val2)
                    continue
                if t == '-':
                    stack.append(val2-val1)
                    continue
                if t == '*':
                    stack.append(val1*val2)
                    continue
                if t == '/':
                    stack.append(int(val2/val1))
                    continue
            else:
                stack.append(int(t))
        return stack[0]  
