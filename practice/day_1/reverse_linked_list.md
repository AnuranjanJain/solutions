# Reverse Linked List

## Problem Description

Given the head of a singly linked list, reverse the list, and return the reversed list.

 
Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


Example 2:


Input: head = [1,2]
Output: [2,1]


Example 3:


Input: head = []
Output: []


 
Constraints:


	The number of nodes in the list is the range [0, 5000].
	-5000 <= Node.val <= 5000


 
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/reverse-linked-list/
- **Topics:** Linked List, Recursion

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=None,head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
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

