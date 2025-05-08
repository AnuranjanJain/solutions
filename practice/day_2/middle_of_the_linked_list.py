# LeetCode Problem: Middle Of The Linked List
# URL: https://leetcode.com/problems/middle-of-the-linked-list/
# Day: 2
# Difficulty: Easy
# Date: 2025-05-01
# Status: Solved

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
