# LeetCode Problem: Diameter of Binary Tree
# URL: https://leetcode.com/problems/diameter-of-binary-tree/
# Day: 30
# Difficulty: Easy
# Date: 2025-05-29
# Status: Solved

class Solution(object):
    def diameterOfBinaryTree(self, root):
        def diameter(node, res):
            if not node:
                return 0

            left = diameter(node.left, res)
            right = diameter(node.right, res)

            res[0] = max(res[0], left + right)

            return max(left, right) + 1

        res = [0]

        diameter(root, res)
    
        return res[0]