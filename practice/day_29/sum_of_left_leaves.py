# LeetCode Problem: Sum of Left Leaves
# URL: https://leetcode.com/problems/sum-of-left-leaves/description/
# Day: 29
# Difficulty: Easy
# Date: 2025-05-28
# Status: Solved

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append((root, "")) 
        tot = 0

        while queue:
            node, direction = queue.popleft()

            if direction == "left" and not node.left and not node.right:
                tot += node.val

            if node.left:
                queue.append((node.left, "left"))
            if node.right:
                queue.append((node.right, "right"))

        return tot