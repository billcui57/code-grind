# Best Time to Buy and Sell Stock

## Link

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Where

Leetcode

## Difficulty

Easy

## Description

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Solution Main Idea

Keep a pointer for low and high. If price[low] < price[high] then check if its more than maxProfit. In either case move high pointer to the right. Else if price[low] > price[high] then set low pointer to equal high pointer and move high pointer to the right. Do this while both pointers are in range. Report highest profit


## Code

```python
def maxProfit(self, prices: List[int]) -> int:

    curMaxProfit = 0
    lowIndex = 0
    highIndex = 0

    while highIndex < len(prices) and lowIndex < len(prices):
        highPrice = prices[highIndex]
        lowPrice = prices[lowIndex]

        if lowPrice < highPrice:
            if highPrice - lowPrice > curMaxProfit:
                curMaxProfit = highPrice - lowPrice
            highIndex += 1
        else:
            lowIndex = highIndex
            highIndex += 1

    return curMaxProfit

```
