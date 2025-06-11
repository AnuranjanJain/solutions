# LeetCode Problem: Kth Smallest Element in a BST
# URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Day: 43
# Difficulty: Medium
# Date: 2025-06-11
# Status: Solved

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest=[]
        def transverse(root):
            if root==None: return 
            left=transverse(root.left)
            smallest.append(root.val)
            right=transverse(root.right)
        transverse(root)
        return smallest[k-1]
                
