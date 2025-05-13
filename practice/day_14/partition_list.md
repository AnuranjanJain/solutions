# Partition List

## Problem Description

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 
Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]


Example 2:


Input: head = [2,1], x = 2
Output: [1,2]


 
Constraints:


	The number of nodes in the list is in the range [0, 200].
	-100 <= Node.val <= 100
	-200 <= x <= 200

## Problem Details

- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/partition-list/
- **Topics:** Linked List, Two Pointers

## Solution Approach

This problem is solved using a sorting-based approach. Sorting the input data allows for more efficient processing and often simplifies the overall solution strategy.

## Step-by-Step Explanation

1. Apply a sorting algorithm to order the input data.
2. Process the sorted data to solve the problem efficiently.
3. The sorting step simplifies subsequent operations by providing a structured order to the elements.

## Code Implementation

```python
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0) 
        after_head = ListNode(0)  

        before = before_head
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None           
        before.next = after_head.next 

        return before_head.next
```

## Complexity Analysis

- **Time Complexity**: O(n log n) where n is the size of the input, due to the sorting operation.
- **Space Complexity**: O(1) to O(n) depending on the sorting algorithm used.

## Optimizations and Alternatives

- Using a specialized data structure like a heap or balanced tree could be more efficient for specific operations.
- For small inputs or nearly sorted data, simpler sorting algorithms like insertion sort might be more efficient.


## Key Takeaways

- Sorting often simplifies subsequent operations and can reduce overall time complexity.
- Consider whether partial sorting or other data structures might be more efficient for the specific requirements.
- Breaking down the problem into smaller steps often leads to a clearer solution.
- Consider the trade-offs between time complexity, space complexity, and code readability.

