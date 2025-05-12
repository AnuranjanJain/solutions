# Count Odd Numbers In An Interval Range

## Problem Description

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 
Example 1:


Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:


Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

 
Constraints:


	0 <= low <= high <= 10^9

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
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
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)
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

