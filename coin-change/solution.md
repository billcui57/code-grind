# Coin Change

## Link

https://leetcode.com/problems/coin-change/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

## Solution Main Idea

DP. Let A[i] denote the least amount of coins needed to fulfill amount $i$. $A[i] = min(A[i], 1+A[i-coin])$ Let $A[i]$ be the minimum of using that coin or not using that coin.
