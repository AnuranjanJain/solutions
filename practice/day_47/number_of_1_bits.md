# Number Of 1 Bits

## Problem Description

Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 
Example 1:


Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.


Example 2:


Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.


Example 3:


Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.


 
Constraints:


	1 <= n <= 231 - 1


 
Follow up: If this function is called many times, how would you optimize it?

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/number-of-1-bits/description/
- **Topics:** Divide and Conquer, Bit Manipulation

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
    def hammingWeight(self, n: int) -> int:
        no=list(bin(n))
        ans=0
        for i in no[2:]:
            if i=="1":
                ans+=1
        return ans
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

