# Sum Root To Leaf Numbers

## Problem Description

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.


	For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.


Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 
Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.


Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


 
Constraints:


	The number of nodes in the tree is in the range [1, 1000].
	0 <= Node.val <= 9
	The depth of the tree will not exceed 10.

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
- **Topics:** Tree, Depth-First Search, Binary Tree

## Solution Approach

This problem is solved using a depth-first search (DFS) approach. DFS explores as far as possible along each branch before backtracking, which is ideal for traversing or searching in tree or graph structures.

## Step-by-Step Explanation

1. Define a DFS function to explore the structure.
2. Use a stack (or recursion) to keep track of nodes to visit.
3. For each node, process it and mark it as visited.
4. Explore all unvisited neighbors by adding them to the stack.
5. Continue until the stack is empty or the goal is reached.

## Code Implementation

```python
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, node: TreeNode, num: int) -> int:
        if not node:
            return 0
        if not node.left and not node.right:
            return num * 10 + node.val
        return self.dfs(node.left, num * 10 + node.val) + self.dfs(node.right, num * 10 + node.val)
```

## Complexity Analysis

- **Time Complexity**: O(V + E) where V is the number of vertices (nodes) and E is the number of edges in the graph or tree.
- **Space Complexity**: O(V) in the worst case, to store the visited nodes and the recursion stack or queue.

## Optimizations and Alternatives

- Breadth-first search (BFS) could be used instead, which might be preferable if finding the shortest path is a priority.
- An iterative approach with an explicit stack could replace the recursive implementation to avoid stack overflow for deep structures.


## Key Takeaways

- Graph traversal algorithms require careful handling of visited nodes to avoid cycles.
- The choice between DFS and BFS depends on the problem requirements (depth exploration vs. shortest path).
- Breaking down the problem into smaller steps often leads to a clearer solution.
- Consider the trade-offs between time complexity, space complexity, and code readability.

