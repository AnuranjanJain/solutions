# LeetCode Problem: Palindrome Linked List
# URL: https://leetcode.com/problems/palindrome-linked-list/
# Day: 5
# Difficulty: Easy
# Date: 2025-05-04
# Status: Solved

class Solution:
   def isPalindrome(self, head: Optional[ListNode]) -> bool:
    rev = []
    og = []
    curr = head
    
    while curr:
        og.append(curr.val)
        curr = curr.next
    
    rev = og[::-1]
    return og == rev
