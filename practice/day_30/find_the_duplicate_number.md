# Find The Duplicate Number

## Problem Description

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 
Example 1:


Input: nums = [1,3,4,2,2]
Output: 2


Example 2:


Input: nums = [3,1,3,4,2]
Output: 3


Example 3:


Input: nums = [3,3,3,3,3]
Output: 3

 
Constraints:


	1 <= n <= 105
	nums.length == n + 1
	1 <= nums[i] <= n
	All the integers in nums appear only once except for precisely one integer which appears two or more times.


 
Follow up:


	How can we prove that at least one duplicate number must exist in nums?
	Can you solve the problem in linear runtime complexity?

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/find-the-duplicate-number/description/
- **Topics:** Array, Two Pointers, Binary Search, Bit Manipulation

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
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ind = abs(nums[i])
            if nums[ind] < 0:
                return ind
            nums[ind] = -nums[ind]
        return -1
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

