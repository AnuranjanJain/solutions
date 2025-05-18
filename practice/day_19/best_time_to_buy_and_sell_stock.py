# LeetCode Problem: Best Time to Buy and Sell Stock
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Day: 19
# Difficulty: Easy
# Date: 2025-05-18
# Status: Solved

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price

            current_profit = price - min_price

            if current_profit > max_profit:
                max_profit = current_profit
            
        return max_profit