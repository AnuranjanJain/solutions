# Delete Node In A Linked List

## Problem Description

There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:


	The value of the given node should not exist in the linked list.
	The number of nodes in the linked list should decrease by one.
	All the values before node should be in the same order.
	All the values after node should be in the same order.


Custom testing:


	For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
	We will build the linked list and pass the node to your function.
	The output will be the entire list after calling your function.


 
Example 1:


Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.


Example 2:


Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


 
Constraints:


	The number of the nodes in the given list is in the range [2, 1000].
	-1000 <= Node.val <= 1000
	The value of each node in the list is unique.
	The node to be deleted is in the list and is not a tail node.

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/delete-node-in-a-linked-list/description/
- **Topics:** Linked List

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
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
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

