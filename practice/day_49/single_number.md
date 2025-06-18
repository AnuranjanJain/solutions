# Single Number

## Problem Description

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 
Example 1:


Input: nums = [2,2,1]

Output: 1


Example 2:


Input: nums = [4,1,2,1,2]

Output: 4


Example 3:


Input: nums = [1]

Output: 1


 
Constraints:


	1 <= nums.length <= 3 * 104
	-3 * 104 <= nums[i] <= 3 * 104
	Each element in the array appears twice except for one element which appears only once.

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/single-number/description/
- **Topics:** Array, Bit Manipulation

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
    def singleNumber(self, nums: List[int]):
        r=0
        for i in nums:
            r=r^i 
        return r
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

