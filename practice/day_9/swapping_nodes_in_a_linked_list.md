# Swapping Nodes In A Linked List

## Problem Description

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 
Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]


Example 2:


Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]


 
Constraints:


	The number of nodes in the list is n.
	1 <= k <= n <= 105
	0 <= Node.val <= 100

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
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
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        first = head
        for _ in range(k - 1):
            first = first.next
        
        second = head
        for _ in range(length - k):
            second = second.next
        
        first.val, second.val = second.val, first.val
        
        return head
```

## Complexity Analysis

- **Time Complexity**: O(n²) where n is the size of the input, due to the nested loops.
- **Space Complexity**: O(1) constant extra space

## Optimizations and Alternatives

- A more space-efficient approach might be possible by optimizing the data structures used.
- A different algorithm paradigm (like divide-and-conquer or greedy) could provide a valid solution with different trade-offs.


## Key Takeaways

- Breaking down the problem into smaller steps often leads to a clearer solution.
- Consider the trade-offs between time complexity, space complexity, and code readability.

