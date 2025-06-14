# LeetCode Problem: Prime Number of Set Bits in Binary Representation
# URL: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
# Day: 46
# Difficulty: Easy
# Date: 2025-06-14
# Status: Solved

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
    
        def find_prime(value):
            p = 2
            if value == 1:
                return False
            if value == 2:
                return True
            while p<=int(sqrt(value))+1:
                if value%p == 0:
                    return False
                p+=1
            return True
            
        for i in range(left,right+1):
            a = bin(i)[2:]
            one = a.count('1')
            if find_prime(one):
                count+=1
        return count