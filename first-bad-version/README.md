# First Bad Version

## Link

https://leetcode.com/problems/first-bad-version/

## Where

Leetcode

## Difficulty

Easy

## Description

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

## Solution Main Idea

Binary search. If it is a bad version we set tail to be middle to not lose the first bad version
