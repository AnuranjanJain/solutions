# LeetCode Problem: Flatten Binary Tree to Linked List
# URL: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Day: 35
# Difficulty: Medium
# Date: 2025-06-02
# Status: Solved

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr=root
        while curr:
            if curr.left!=None:
                prev=curr.left
                while prev.right:
                    prev=prev.right
                prev.right=curr.right
                curr.right=curr.left
                curr.left=None
            curr=curr.right