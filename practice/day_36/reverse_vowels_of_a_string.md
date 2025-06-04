# Reverse Vowels Of A String

## Problem Description

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 
Example 1:


Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".


Example 2:


Input: s = "leetcode"

Output: "leotcede"


 
Constraints:


	1 <= s.length <= 3 * 105
	s consist of printable ASCII characters.

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/reverse-vowels-of-a-string/description/
- **Topics:** Two Pointers, String

## Solution Approach

This problem is solved using a binary search approach. Binary search is an efficient algorithm for finding an element in a sorted array by repeatedly dividing the search interval in half.

## Step-by-Step Explanation

1. Initialize left and right pointers to the start and end of the array.
2. While left <= right, compute the middle index.
3. Compare the middle element with the target value.
4. If the middle element equals the target, return the index.
5. If the middle element is greater than the target, search the left half.
6. If the middle element is less than the target, search the right half.
7. If the element is not found, return an appropriate indicator.

## Code Implementation

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) - 1
    
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
    
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
        return ''.join(s)
```

## Complexity Analysis

- **Time Complexity**: O(log n) where n is the size of the input array. Binary search divides the search space in half with each step.
- **Space Complexity**: O(1) constant extra space is used.

## Optimizations and Alternatives

- A linear search approach could also work but would be less efficient with O(n) time complexity.
- A hash map could provide O(1) lookups but requires O(n) space and preprocessing time.


## Key Takeaways

- Binary search is most effective on sorted data and reduces the search space by half in each step.
- Always check boundary conditions and how to handle duplicates when implementing binary search.
- Breaking down the problem into smaller steps often leads to a clearer solution.
- Consider the trade-offs between time complexity, space complexity, and code readability.

