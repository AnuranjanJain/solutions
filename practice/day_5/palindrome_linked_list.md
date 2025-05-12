# Palindrome Linked List

## Problem Description

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 
Example 1:


Input: head = [1,2,2,1]
Output: true


Example 2:


Input: head = [1,2]
Output: false


 
Constraints:


	The number of nodes in the list is in the range [1, 105].
	0 <= Node.val <= 9


 
Follow up: Could you do it in O(n) time and O(1) space?

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/palindrome-linked-list/
- **Topics:** Linked List, Two Pointers, Stack, Recursion

## Solution Approach

This problem requires a methodical approach to handle different cases and edge conditions. The solution implements a careful algorithm to process the input efficiently.

## Step-by-Step Explanation

1. Analyze the problem requirements and edge cases.
2. Choose appropriate data structures for efficient operations.
3. Implement the core algorithm to process the input.
4. Handle edge cases and specific conditions.
5. Optimize the solution for better performance.
6. Build and return the required result.

## Code Implementation

```python
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
```

## Complexity Analysis

- **Time Complexity**: O(n) where n is the size of the input
- **Space Complexity**: O(1) constant extra space

## Optimizations and Alternatives

- A more space-efficient approach might be possible by optimizing the data structures used.
- A different algorithm paradigm (like divide-and-conquer or greedy) could provide a valid solution with different trade-offs.


## Key Takeaways

- Breaking down the problem into smaller steps often leads to a clearer solution.
- Consider the trade-offs between time complexity, space complexity, and code readability.

