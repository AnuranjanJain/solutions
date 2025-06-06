# LeetCode Problem: Remove Linked List Elements
# URL: https://leetcode.com/problems/remove-linked-list-elements/description/
# Day: 6
# Difficulty: Medium
# Date: 2025-05-05
# Status: Solved
# Solution for Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/description/

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
