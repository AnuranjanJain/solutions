# LeetCode Problem: Hamming Distance
# URL: https://leetcode.com/problems/hamming-distance/
# Day: 48
# Difficulty: Easy
# Date: 2025-06-16
# Status: Solved

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        return bin(xor).count('1')