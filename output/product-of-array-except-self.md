# product-of-array-except-self

## Link

https://leetcode.com/problems/product-of-array-except-self/

## Where

Leetcode

## Difficulty

Easy

## Description

Given an integer array $nums$, return an array $answer$ such that $answer[i]$ is equal to the product of all the elements of $nums$ except $nums[i]$.

The product of any prefix or suffix of $nums$ is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Solution Main Idea

Keep track of a suffix and prefix array. Prefix[i] = product of the prefix of num bounded by i excluding i. Suffix[i] = product of suffix of num bounded by i excluding i. $answer[i] = prefix[i] = suffix[i]$


## Code

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    prefixProduct = {}
    prefixProduct[0] = 1
    for i in range(1, len(nums)):
        prefixProduct[i] = prefixProduct[i-1] * nums[i-1]

    suffixProduct = {}
    suffixProduct[len(nums) - 1] = 1
    for i in reversed(range(0, len(nums)-1)):
        suffixProduct[i] = suffixProduct[i+1] * nums[i+1]

    answer = [None] * len(nums)
    for i in range(0, len(nums)):
        answer[i] = prefixProduct[i] * suffixProduct[i]

    return answer

```
