# Nth Digit

## Problem Description

Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

 
Example 1:


Input: n = 3
Output: 3


Example 2:


Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


 
Constraints:


	1 <= n <= 231 - 1

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/nth-digit/description/
- **Topics:** Math, Binary Search

## Solution Approach

This problem is solved using careful iteration through the input. The solution tracks necessary values and builds the result incrementally.

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
    def findNthDigit(self, n: int) -> int:
        length, count, start = 1, 9, 1

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        num = start + (n - 1) // length
        return int(str(num)[(n - 1) % length])
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

