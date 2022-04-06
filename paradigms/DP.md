# Dynamic Programming

## When

Useful for when you are dealing with finding the optimal solution given a constraint, or the number of solutions given a constraint, or if there is a solution given a constraint, in an array or string.

## How to use

Let $A[i]$ be the optimal/number-of solution for a prefix of the array/string ending at index $i$. Or a suffix of the array/string beginning at index $i$

Think in terms of take or not take. For each $A[i]$ you're finding the maximum of the values of $A$ at indices that represent the optimal/number of solution of the string/array if you had taken, and had not taken a decision at $i$

## Thoughts

DP is a mindset of partitioning/breaking the input up into subproblems that can either build on top of each other (See longest-increasing-subsequence), or mutually exclusive and much easier to solve on their own and compared (See longest-consecutive-sequence)

The hardest part of DP is finding that partition.
