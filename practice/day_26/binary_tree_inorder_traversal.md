# Binary Tree Inorder Traversal

## Problem Description

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 
Example 1:


Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:




Example 2:


Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:




Example 3:


Input: root = []

Output: []


Example 4:


Input: root = [1]

Output: [1]


 
Constraints:


	The number of nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100


 
Follow up: Recursive solution is trivial, could you do it iteratively?

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/binary-tree-inorder-traversal/description/
- **Topics:** Stack, Tree, Depth-First Search, Binary Tree

## Solution Approach

This problem involves constructing a result based on the given input. The solution processes the input and builds the required output following the problem specifications.

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            result.append(current_node.val)
            if current_node.right:
                traverse(current_node.right)
        if root:
            traverse(root)
        return result
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

