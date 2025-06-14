# Find Center Of Star Graph

## Problem Description

There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 
Example 1:


Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.


Example 2:


Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1


 
Constraints:


	3 <= n <= 105
	edges.length == n - 1
	edges[i].length == 2
	1 <= ui, vi <= n
	ui != vi
	The given edges represent a valid star graph.

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/find-center-of-star-graph/
- **Topics:** Graph

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
    def findCenter(self, edges: List[List[int]]) -> int:
        i, j = edges[0][0], edges[0][1]
        if i in edges[1]: return i
        return j
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

