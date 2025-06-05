# LeetCode Problem: Binary Tree Zigzag Level Order Traversal
# URL: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
# Day: 37
# Difficulty: Medium
# Date: 2025-06-05
# Status: Solved

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        if not root:
            return res
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            
            if len(res) % 2 == 0:
                res.append(level)
            else:
                res.append(level[::-1])
        return res