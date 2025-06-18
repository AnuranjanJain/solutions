# Count Primes

## Problem Description

Given an integer n, return the number of prime numbers that are strictly less than n.

 
Example 1:


Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


Example 2:


Input: n = 0
Output: 0


Example 3:


Input: n = 1
Output: 0


 
Constraints:


	0 <= n <= 5 * 106

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/count-primes/
- **Topics:** Array, Math, Enumeration, Number Theory

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
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        p = 2
        while p * p < n:
            if isPrime[p]:
                for multiple in range(p * p, n, p):
                    isPrime[multiple] = False
            p += 1
        return sum(isPrime)
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

