# LeetCode Problem: Reverse Linked List
# URL: https://leetcode.com/problems/reverse-linked-list/
# Day: 1
# Difficulty: Easy
# Date: 2025-04-30
# Status: Solved
# Solution for Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=None,head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev