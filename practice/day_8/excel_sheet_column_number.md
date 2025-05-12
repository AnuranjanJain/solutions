# Excel Sheet Column Number

## Problem Description

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:


A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...


 
Example 1:


Input: columnTitle = "A"
Output: 1


Example 2:


Input: columnTitle = "AB"
Output: 28


Example 3:


Input: columnTitle = "ZY"
Output: 701


 
Constraints:


	1 <= columnTitle.length <= 7
	columnTitle consists only of uppercase English letters.
	columnTitle is in the range ["A", "FXSHRXW"].

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/excel-sheet-column-number/description/
- **Topics:** Math, String

## Solution Approach

This problem involves constructing a result based on the given input. The solution processes the input and builds the required output following the problem specifications.

## Step-by-Step Explanation

1. Analyze the problem requirements and edge cases.
2. Choose appropriate data structures for efficient operations.
3. Implement the core algorithm to process the input.
4. Handle edge cases and specific conditions.
5. Optimize the solution for better performance.
6. Build and return the required result.

## Code Implementation

```python
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result
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

