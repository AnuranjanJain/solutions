# LeetCode Problem: Reverse Linked List
# URL: https://leetcode.com/problems/reverse-linked-list/
# Day: 1
# Difficulty: Easy
# Date: 2025-04-30
# Status: Solved


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=None,head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev