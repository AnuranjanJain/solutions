# LeetCode Problem: Sign of the Product of an Array
# URL: https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
# Day: 13
# Difficulty: Easy
# Date: 2025-05-12
# Status: Solved

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prd=1
        for num in nums:
            if num==0:
                prd=0
            else:
                prd=num*prd
        def signFunc(num):
            if num<0:
                return -1
            elif num==0:
                return 0
            else:
                return 1
        return signFunc(prd)
