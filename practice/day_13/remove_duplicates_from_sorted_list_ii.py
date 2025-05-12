# LeetCode Problem: Remove Duplicates from Sorted List II
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
# Day: 13
# Difficulty: Medium
# Date: 2025-05-12
# Status: Solved

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next