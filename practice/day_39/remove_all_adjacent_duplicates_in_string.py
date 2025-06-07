# LeetCode Problem: Remove All Adjacent Duplicates In String
# URL: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Day: 39
# Difficulty: Easy
# Date: 2025-06-07
# Status: Solved

class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for c in s:
            if st and st[-1] == c:
                st.pop()
            else:
                st.append(c)
        return ''.join(st)