# LeetCode Problem: Merge Two Sorted Lists
# URL: https://leetcode.com/problems/merge-two-sorted-lists/
# Day: 3
# Difficulty: Easy
# Date: 2025-05-02
# Status: Solved
# Solution for Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next