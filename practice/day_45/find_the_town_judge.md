# Find The Town Judge

## Problem Description

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:


	The town judge trusts nobody.
	Everybody (except for the town judge) trusts the town judge.
	There is exactly one person that satisfies properties 1 and 2.


You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 
Example 1:


Input: n = 2, trust = [[1,2]]
Output: 2


Example 2:


Input: n = 3, trust = [[1,3],[2,3]]
Output: 3


Example 3:


Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1


 
Constraints:


	1 <= n <= 1000
	0 <= trust.length <= 104
	trust[i].length == 2
	All the pairs of trust are unique.
	ai != bi
	1 <= ai, bi <= n

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/find-the-town-judge/description/
- **Topics:** Array, Hash Table, Graph

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
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        counts = [0] * (n + 1)
        for a, b in trust:
            counts[a] -= 1
            counts[b] += 1
        for i in range(1, n + 1):
            if counts[i] == n - 1:
                return i
        return -1
```

## Complexity Analysis

- **Time Complexity**: O(n²) where n is the size of the input, due to the nested loops.
- **Space Complexity**: O(1) constant extra space

## Optimizations and Alternatives

- A more space-efficient approach might be possible by optimizing the data structures used.
- A different algorithm paradigm (like divide-and-conquer or greedy) could provide a valid solution with different trade-offs.


## Key Takeaways

- Breaking down the problem into smaller steps often leads to a clearer solution.
- Consider the trade-offs between time complexity, space complexity, and code readability.

