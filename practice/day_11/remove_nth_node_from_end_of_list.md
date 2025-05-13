# Remove Nth Node From End Of List

## Problem Description

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 
Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


Example 2:


Input: head = [1], n = 1
Output: []


Example 3:


Input: head = [1,2], n = 1
Output: [1]


 
Constraints:


	The number of nodes in the list is sz.
	1 <= sz <= 30
	0 <= Node.val <= 100
	1 <= n <= sz


 
Follow up: Could you do this in one pass?

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
- **Topics:** Linked List, Two Pointers

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        curr = head
        while curr:
            curr = curr.next
            k += 1
        if k - n == 0:
            return head.next
        curr = head
        for _ in range(1, k - n):
            curr = curr.next
        curr.next = curr.next.next
        return head
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

