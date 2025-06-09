# Delete Node In A Bst

## Problem Description

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:


	Search for a node to remove.
	If the node is found, delete the node.


 
Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.



Example 2:


Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.


Example 3:


Input: root = [], key = 0
Output: []


 
Constraints:


	The number of nodes in the tree is in the range [0, 104].
	-105 <= Node.val <= 105
	Each node has a unique value.
	root is a valid binary search tree.
	-105 <= key <= 105


 
Follow up: Could you solve it with time complexity O(height of tree)?

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/delete-node-in-a-bst/description/
- **Topics:** Tree, Binary Search Tree, Binary Tree

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
    def findmin(self,root:Optional[TreeNode])->int:
        if root.left:
            return self.findmin(root.left)
        return root.val
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val==key:
            if not root.left and not root.right:
                root=None
            elif not root.left and root.right:
                root=root.right
            elif root.left and not root.right:
                root=root.left
            else:
                m=self.findmin(root.right)
                root.val=m
                root.right=self.deleteNode(root.right,m)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            root.left=self.deleteNode(root.left,key)
        return root
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

