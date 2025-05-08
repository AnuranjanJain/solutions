# LeetCode Problem: Rotate List
# URL: https://leetcode.com/problems/rotate-list/
# Day: 7
# Difficulty: Medium
# Date: 2025-05-06
# Status: Solved
# Solution for Rotate List
# https://leetcode.com/problems/rotate-list/

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        count = 1
        temp = head
        while temp.next:
            temp = temp.next
            count += 1

        k = k % count
        if k == 0:
            return head

        temp.next = head

        steps = count - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
