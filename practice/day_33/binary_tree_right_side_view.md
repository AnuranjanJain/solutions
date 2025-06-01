# Binary Tree Right Side View

## Problem Description

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 
Example 1:


Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:




Example 2:


Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:




Example 3:


Input: root = [1,null,3]

Output: [1,3]


Example 4:


Input: root = []

Output: []


 
Constraints:


	The number of nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/binary-tree-right-side-view/description/
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=[[root]]
        ans=[root.val]
        while queue:
            currentLevel=queue.pop(0)
            nextLevel=[]
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if nextLevel:
                ans.append(nextLevel[-1].val)
                queue.append(nextLevel)
        return ans
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

