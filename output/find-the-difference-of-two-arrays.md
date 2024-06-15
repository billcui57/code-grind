# Find the Difference of Two Arrays

## Link
https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

## Where
Leetcode

## Difficulty
Easy

## Description
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.


## Solution Main Idea
Sets



## Code

```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1Set = set(nums1)
        nums2Set = set(nums2)

        answer2 = set()
        answer1 = set()

        for num in nums1:
            if num not in nums2Set:
                answer1.add(num)
        for num in nums2:
            if num not in nums1Set:
                answer2.add(num)
        return [list(answer1), list(answer2)]

```
