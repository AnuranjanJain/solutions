# LeetCode Problem: Linked List Cycle
# URL: https://leetcode.com/problems/linked-list-cycle/
# Day: 4
# Difficulty: Easy
# Date: 2025-05-03
# Status: Solved

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          
            fast = fast.next.next     
            if slow == fast:
                return True           
        return False        