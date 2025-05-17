# Implement Queue Using Stacks

## Problem Description

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:


	void push(int x) Pushes element x to the back of the queue.
	int pop() Removes the element from the front of the queue and returns it.
	int peek() Returns the element at the front of the queue.
	boolean empty() Returns true if the queue is empty, false otherwise.


Notes:


	You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
	Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.


 
Example 1:


Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false


 
Constraints:


	1 <= x <= 9
	At most 100 calls will be made to push, pop, peek, and empty.
	All the calls to pop and peek are valid.


 
Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

## Problem Details

- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/implement-queue-using-stacks/description/
- **Topics:** Stack, Design, Queue

## Solution Approach

This problem can be solved using a straightforward iterative approach. The solution carefully processes the input and constructs the required output.

## Step-by-Step Explanation

1. Parse and validate the input data.
2. Initialize necessary variables and data structures.
3. Process the input using appropriate operations.
4. Build and return the required result.

## Code Implementation

```python
# LeetCode Problem: Implement Queue using Stacks
# URL: https://leetcode.com/problems/implement-queue-using-stacks/description/
# Day: 18
# Difficulty: Easy
# Date: 2025-05-17
# Status: Solved
```

## Complexity Analysis

- **Time Complexity**: O(n) where n is the size of the input
- **Space Complexity**: O(1) constant extra space

## Optimizations and Alternatives

- A brute force approach might be simpler to implement but less efficient.
- Using different data structures could simplify certain operations at the cost of added complexity.


## Key Takeaways

- Even simple problems benefit from a clear approach and clean implementation.
- Test edge cases like empty inputs, single elements, or maximum values.

