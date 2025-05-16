# LeetCode Problem: Min Stack
# URL: https://leetcode.com/problems/min-stack/description/
# Day: 17
# Difficulty: Medium
# Date: 2025-05-16
# Status: Solved

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1],val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
