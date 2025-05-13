# Factorial Trailing Zeroes

## Problem Description

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 
Example 1:


Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.


Example 2:


Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.


Example 3:


Input: n = 0
Output: 0


 
Constraints:


	0 <= n <= 104


 
Follow up: Could you write a solution that works in logarithmic time complexity?

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/factorial-trailing-zeroes/description/
- **Topics:** Math

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
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count
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

