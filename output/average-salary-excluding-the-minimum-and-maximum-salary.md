# Average Salary Excluding the Minimum and Maximum Salary

## Link
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/

## Where
Leetcode

## Difficulty
Easy

## Description
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

## Solution Main Idea
Find min and max and remove it


## Code

```python
class Solution:
    def average(self, salary: List[int]) -> float:

        cumSum = 0
        maxSal = 0
        minSal = inf

        for sal in salary:
            cumSum += sal
            maxSal = max(maxSal,sal)
            minSal = min(minSal, sal)
        

        return (cumSum-maxSal-minSal)/(len(salary)-2)
```
