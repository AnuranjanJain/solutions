# Sum Of Left Leaves

## Problem Description

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.


Example 2:


Input: root = [1]
Output: 0


 
Constraints:


	The number of nodes in the tree is in the range [1, 1000].
	-1000 <= Node.val <= 1000

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/sum-of-left-leaves/description/
- **Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

## Solution Approach

This problem is solved using a breadth-first search (BFS) approach. BFS explores all neighbor nodes at the present depth before moving to nodes at the next depth level, making it suitable for finding shortest paths in unweighted graphs.

## Step-by-Step Explanation

1. Initialize a queue with the starting node(s).
2. While the queue is not empty, dequeue a node.
3. Process the node and mark it as visited.
4. Enqueue all unvisited neighbors of the current node.
5. Continue until the queue is empty or the goal is reached.

## Code Implementation

```python
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append((root, "")) 
        tot = 0

        while queue:
            node, direction = queue.popleft()

            if direction == "left" and not node.left and not node.right:
                tot += node.val

            if node.left:
                queue.append((node.left, "left"))
            if node.right:
                queue.append((node.right, "right"))

        return tot
```

## Complexity Analysis

- **Time Complexity**: O(V + E) where V is the number of vertices (nodes) and E is the number of edges in the graph or tree.
- **Space Complexity**: O(V) in the worst case, to store the visited nodes and the recursion stack or queue.

## Optimizations and Alternatives

- Depth-first search (DFS) could be used instead, which might use less memory in some cases.
- A bidirectional BFS could be more efficient for certain path-finding problems.


## Key Takeaways

- Graph traversal algorithms require careful handling of visited nodes to avoid cycles.
- The choice between DFS and BFS depends on the problem requirements (depth exploration vs. shortest path).
- Breaking down the problem into smaller steps often leads to a clearer solution.
- Consider the trade-offs between time complexity, space complexity, and code readability.

