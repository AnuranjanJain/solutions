# LeetCode Problem: Insert Greatest Common Divisors In Linked List
# URL: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/submissions/1630980480/
# Day: 12
# Difficulty: Medium
# Date: 2025-05-11
# Status: Solved
# Solution for Insert Greatest Common Divisors In Linked List
# 

# Solution for Insert Greatest Common Divisors in Linked List
# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/submissions/1630980480/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            next_node = curr.next
            g = gcd(curr.val, next_node.val)
            new_node = ListNode(g)
            curr.next = new_node
            new_node.next = next_node
            curr = next_node

        return head
