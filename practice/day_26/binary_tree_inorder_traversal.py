# LeetCode Problem: Binary Tree Inorder Traversal
# URL: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Day: 26
# Difficulty: Easy
# Date: 2025-05-25
# Status: Solved

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            result.append(current_node.val)
            if current_node.right:
                traverse(current_node.right)
        if root:
            traverse(root)
        return result