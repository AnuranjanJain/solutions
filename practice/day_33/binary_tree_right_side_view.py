# LeetCode Problem: Binary Tree Right Side View
# URL: https://leetcode.com/problems/binary-tree-right-side-view/description/
# Day: 33
# Difficulty: Medium
# Date: 2025-06-01
# Status: Solved

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=[[root]]
        ans=[root.val]
        while queue:
            currentLevel=queue.pop(0)
            nextLevel=[]
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if nextLevel:
                ans.append(nextLevel[-1].val)
                queue.append(nextLevel)
        return ans