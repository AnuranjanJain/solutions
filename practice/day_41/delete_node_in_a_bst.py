# LeetCode Problem: Delete Node in a BST
# URL: https://leetcode.com/problems/delete-node-in-a-bst/description/
# Day: 41
# Difficulty: Medium
# Date: 2025-06-09
# Status: Solved

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findmin(self,root:Optional[TreeNode])->int:
        if root.left:
            return self.findmin(root.left)
        return root.val
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val==key:
            if not root.left and not root.right:
                root=None
            elif not root.left and root.right:
                root=root.right
            elif root.left and not root.right:
                root=root.left
            else:
                m=self.findmin(root.right)
                root.val=m
                root.right=self.deleteNode(root.right,m)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            root.left=self.deleteNode(root.left,key)
        return root