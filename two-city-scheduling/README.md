# Two City Scheduling

## Link

https://leetcode.com/problems/two-city-scheduling/description/

## Where

Leetcode

## Difficulty

Medium

## Description

A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

## Solution Main Idea

Sort by abs diff between two methods, and greedily take the lowest cost of each.
