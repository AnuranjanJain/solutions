# LeetCode Problem: Odd Even Linked List
# URL: https://leetcode.com/problems/odd-even-linked-list/description/
# Day: 8
# Difficulty: Medium
# Date: 2025-05-07
# Status: Solved
# Solution for Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/description/

class Solution(object):
     def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head