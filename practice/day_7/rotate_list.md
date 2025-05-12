# Rotate List

## Problem Description

Given the head of a linked list, rotate the list to the right by k places.

 
Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]


Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


 
Constraints:


	The number of nodes in the list is in the range [0, 500].
	-100 <= Node.val <= 100
	0 <= k <= 2 * 109

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/rotate-list/
- **Topics:** Linked List, Two Pointers

## Solution Approach

This problem is solved using careful iteration through the input. The solution tracks necessary values and builds the result incrementally.

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

