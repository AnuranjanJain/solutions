# Number Of Substrings Containing All Three Characters

## Problem Description

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 
Example 1:


Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 


Example 2:


Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 


Example 3:


Input: s = "abc"
Output: 1


 
Constraints:


	3 <= s.length <= 5 x 10^4
	s only consists of a, b or c characters.

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
- **Topics:** Hash Table, String, Sliding Window

## Solution Approach

This problem is solved using careful iteration through the input. The solution tracks necessary values and builds the result incrementally. The solution also incorporates a construction technique.

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
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        res = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                res += len(s) - right
                count[s[left]] -= 1
                left += 1
        return res
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

