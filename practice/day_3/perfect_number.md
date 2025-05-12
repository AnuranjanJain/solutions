# Perfect Number

## Problem Description

A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

 
Example 1:


Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.


Example 2:


Input: num = 7
Output: false


 
Constraints:


	1 <= num <= 108

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/perfect-number/
- **Topics:** Math

## Solution Approach

This problem is solved using a hash map (dictionary) for efficient lookups. Hash maps provide O(1) average case time complexity for insertions, deletions, and lookups.

## Step-by-Step Explanation

1. Initialize a hash map (dictionary) to store key-value pairs.
2. Process the input, utilizing the hash map for efficient lookups, insertions, and deletions.
3. The hash map provides O(1) average time complexity for these operations, making the overall solution efficient.

## Code Implementation

```python
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in {6, 28, 496, 8128, 33550336}
```

## Complexity Analysis

- **Time Complexity**: O(n) where n is the size of the input. Hash map operations are O(1) on average.
- **Space Complexity**: O(n) to store the hash map contents.

## Optimizations and Alternatives

- A sorted array with binary search could provide O(log n) lookups with potentially better space efficiency.
- A trie data structure could be more efficient for string-related problems.


## Key Takeaways

- Hash maps provide O(1) average-case lookups but require good hash functions to avoid collisions.
- Consider memory usage when using hash maps for large inputs.
- Breaking down the problem into smaller steps often leads to a clearer solution.
- Consider the trade-offs between time complexity, space complexity, and code readability.

