# LeetCode Problem: Swapping Nodes In A Linked List
# URL: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
# Day: 9
# Difficulty: Medium
# Date: 2025-05-08
# Status: Solved
# Solution for Swapping Nodes In A Linked List
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        first = head
        for _ in range(k - 1):
            first = first.next
        
        second = head
        for _ in range(length - k):
            second = second.next
        
        first.val, second.val = second.val, first.val
        
        return head