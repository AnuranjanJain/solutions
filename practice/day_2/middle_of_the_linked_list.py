# LeetCode Problem: Middle of the Linked List
# URL: https://leetcode.com/problems/middle-of-the-linked-list/
# Day: 2
# Difficulty: Easy
# Date: 2025-05-01
# Status: Solved

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        sliced = values[len(values)//2 :]

        dummy = ListNode(0)
        curr = dummy
        for val in sliced:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
