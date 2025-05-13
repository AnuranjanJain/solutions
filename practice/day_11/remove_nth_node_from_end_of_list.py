
# LeetCode Problem: Remove Nth Node From End Of List
# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Day: 11
# Difficulty: Medium
# Date: 2025-05-10
# Status: Solved
# Solution for Remove Nth Node From End Of List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        curr = head
        while curr:
            curr = curr.next
            k += 1
        if k - n == 0:
            return head.next
        curr = head
        for _ in range(1, k - n):
            curr = curr.next
        curr.next = curr.next.next
        return head