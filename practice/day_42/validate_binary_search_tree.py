# LeetCode Problem: Validate Binary Search Tree
# URL: https://leetcode.com/problems/validate-binary-search-tree/
# Day: 42
# Difficulty: Medium
# Date: 2025-06-10
# Status: Solved

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def inorder(root):
            if root is None: return None
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        return True if arr == list(sorted(set(arr))) else False