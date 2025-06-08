# LeetCode Problem: Lowest Common Ancestor of a Binary Search Tree
# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Day: 40
# Difficulty: Medium
# Date: 2025-06-08
# Status: Solved

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root