# Maximum Profit in Job Scheduling

## Link

https://leetcode.com/problems/maximum-profit-in-job-scheduling/

## Where

Leetcode

## Difficulty

Hard

## Description

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

## Solution Main Idea

Sort by endTime. For each job you take or dont take. If you take, the best profit in that scenario would be the profit of the job + the most profit you can obtain right before that jobs start time. If you dont take, the best profit is the profit of the job before this job. Max over both scenarios.

`A[i] = max(A[i-1],p+A[justBefore])`, where `justBefore` is found via binary search on endTime.
If `justBefore` is not found then `A[i] = max(A[i-1],p)`

`A[i]` denotes the most profit you can obtain from the prefix of the jobs array up to including index `i`


## Code

```python
class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        A = [0] * len(jobs)
        A[0] = jobs[0][2]

        for i in range(1, len(jobs)):
            e, s, p = jobs[i]
            justBefore = (
                bisect.bisect_right(jobs, s, hi=i, key=lambda a: a[0]) - 1
            )  # binary search on jobs to find last index of s, minus 1 to get the last element before s
            if justBefore == -1:
                A[i] = max(A[i - 1], p)
            else:
                A[i] = max(A[i - 1], p + A[justBefore])
        return A[-1]

```
