# Dynamic Programming

## When

Useful for when you are dealing with finding the optimal solution given a constraint, or the number of solutions given a constraint, or if there is a solution given a constraint, in an array or string.

## How to use

Let $A[i]$ be the optimal/number-of solution for a prefix of the array/string ending at index $i$. Or a suffix of the array/string beginning at index $i$

Think in terms of take or not take. For each $A[i]$ you're finding the maximum of the values of $A$ at indices that represent the optimal/number of solution of the string/array if you had taken, and had not taken a decision at $i$

## Thoughts

DP is a mindset of partitioning/breaking the input up into subproblems that can either build on top of each other (See longest-increasing-subsequence), or mutually exclusive and much easier to solve on their own and compared (See longest-consecutive-sequence)

The hardest part of DP is finding that partition.

When you try DP and find that subproblems are actually more complex than the current problem (given all the partitions that you can think of), then should consider BFS

In context of arrays/strings, when building off of subproblems, you either build off the single subproblem directly before, or consider all subproblems before (and if that were the case sometimes binary search can help if things are sorted nicely).
