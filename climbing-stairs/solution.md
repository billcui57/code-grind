# climbing-stairs

## Link

https://leetcode.com/problems/climbing-stairs/

## Where

Leetcode

## Difficulty

Easy

## Description

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Solution Main Idea

Use DP. Let $totalSteps[i]$ denote the num of distinct ways to reach the top when you're at step $i$. step 0 indicates that you're not on the stairs yet. step $n$ indicates you're at the top.

Fill in $totalSteps$ from $n$ to $0$. $totalSteps[i] = totalSteps[i+1] + totalSteps[i+2]$
