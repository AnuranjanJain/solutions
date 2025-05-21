# Minimum Remove To Make Valid Parentheses

## Problem Description

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:


	It is the empty string, contains only lowercase characters, or
	It can be written as AB (A concatenated with B), where A and B are valid strings, or
	It can be written as (A), where A is a valid string.


 
Example 1:


Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.


Example 2:


Input: s = "a)b(c)d"
Output: "ab(c)d"


Example 3:


Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.


 
Constraints:


	1 <= s.length <= 105
	s[i] is either '(' , ')', or lowercase English letter.

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
- **Topics:** String, Stack

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

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''  # remove unmatched ')'

        while stack:
            s[stack.pop()] = ''  # remove unmatched '('

        return ''.join(s)
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

