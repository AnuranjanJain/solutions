# Greatest Common Divisor Of Strings

## Problem Description

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 
Example 1:


Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"


Example 2:


Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"


Example 3:


Input: str1 = "LEET", str2 = "CODE"
Output: ""


 
Constraints:


	1 <= str1.length, str2.length <= 1000
	str1 and str2 consist of English uppercase letters.

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/greatest-common-divisor-of-strings/
- **Topics:** Math, String

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
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1=len(str1)
        l2=len(str2)
        ans=gcd(l1,l2)
        return str1[:ans] if str1+str2==str2+str1 else ""o
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

