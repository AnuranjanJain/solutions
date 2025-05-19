# LeetCode Problem: Delete The Middle Node Of A Linked List
# URL: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
# Day: 10
# Difficulty: Medium
# Date: 2025-05-09
# Status: Solved

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=0
        cur=head
        while cur:
            cur=cur.next
            s+=1
        if s==1:
            return
        temp=head
        prev=None
        for _ in range(s//2):
            prev=temp
            temp=temp.next
        if temp is not  None:
            prev.next=temp.next
        return head