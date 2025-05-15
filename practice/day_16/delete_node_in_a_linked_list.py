# LeetCode Problem: Delete Node in a Linked List
# URL: https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# Day: 16
# Difficulty: Medium
# Date: 2025-05-15
# Status: Solved

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
    