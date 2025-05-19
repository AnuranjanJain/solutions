# Evaluate Reverse Polish Notation

## Problem Description

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:


	The valid operators are '+', '-', '*', and '/'.
	Each operand may be an integer or another expression.
	The division between two integers always truncates toward zero.
	There will not be any division by zero.
	The input represents a valid arithmetic expression in a reverse polish notation.
	The answer and all the intermediate calculations can be represented in a 32-bit integer.


 
Example 1:


Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9


Example 2:


Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6


Example 3:


Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


 
Constraints:


	1 <= tokens.length <= 104
	tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
- **Topics:** Array, Math, Stack

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
    def evalRPN(self, tokens: List[str]) -> int:
        valid=['+','-','*','/']
        stack=[]
        for t in tokens:
            if t in valid:
                val1=stack.pop()
                val2=stack.pop()
                if t == '+':
                    stack.append(val1+val2)
                    continue
                if t == '-':
                    stack.append(val2-val1)
                    continue
                if t == '*':
                    stack.append(val1*val2)
                    continue
                if t == '/':
                    stack.append(int(val2/val1))
                    continue
            else:
                stack.append(int(t))
        return stack[0]
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

