# Longest Valid Parentheses

## Problem Description

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 
Example 1:


Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".


Example 2:


Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".


Example 3:


Input: s = ""
Output: 0


 
Constraints:


	0 <= s.length <= 3 * 104
	s[i] is '(', or ')'.

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/longest-valid-parentheses/description/
- **Topics:** String, Dynamic Programming, Stack

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
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Base index
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        
        return max_length
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

