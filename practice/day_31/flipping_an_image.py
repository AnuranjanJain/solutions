# LeetCode Problem: Flipping an Image
# URL: https://leetcode.com/problems/flipping-an-image/
# Day: 31
# Difficulty: Easy
# Date: 2025-05-30
# Status: Solved

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def flip(arr):
            for i in range(len(arr)):
                arr[i]=arr[i][::-1]
        def invert(arr):
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    if arr[i][j]==0:
                        arr[i][j]=1
                    else:
                        arr[i][j]=0

        flip(image)
        invert(image)
        return image