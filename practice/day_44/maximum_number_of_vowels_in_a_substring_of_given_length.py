# LeetCode Problem: Maximum Number of Vowels in a Substring of Given Length
# URL: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Day: 44
# Difficulty: Medium
# Date: 2025-06-12
# Status: Solved

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = frozenset("aeiou")
        cnt = ans = sum(s[i] in vowels for i in range(k))
        if ans != k:
            for i in range(k, len(s)):
                cnt += (s[i] in vowels) - (s[i - k] in vowels)
                ans = max(cnt, ans)
        return ans