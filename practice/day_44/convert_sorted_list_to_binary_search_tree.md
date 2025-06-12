# Convert Sorted List To Binary Search Tree

## Problem Description

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 
Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.


Example 2:


Input: head = []
Output: []


 
Constraints:


	The number of nodes in head is in the range [0, 2 * 104].
	-105 <= Node.val <= 105

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
- **Topics:** Linked List, Divide and Conquer, Tree, Binary Search Tree, Binary Tree

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
    def make(self,A):
        if A:
            m=len(A)//2
            n =TreeNode(A[m])
            n.left =self.make(A[:m])
            n.right=self.make(A[m+1:])
            return n
    def sortedListToBST(self, head):
        A, n = [], head
        while n:
            A.append(n.val)
            n = n.next
        return self.make(A)
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

