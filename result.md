# 3Sum

## Link

https://leetcode.com/problems/3sum/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an integer array nums, return all the triplets \[nums\[i\],
nums\[j\], nums\[k\]\] such that i != j, i != k, and j != k, and
nums\[i\] + nums\[j\] + nums\[k\] == 0.

Notice that the solution set must not contain duplicate triplets.

## Solution Main Idea

Use twosum to solve threesum. For each index $i$ in $num$, let twoSum
find the two indices $j$, $k$ in $num[i+1:]$ such that
$num[j] + num[k] = -num[i]$. Store these triplets in a seen table. A
seen table is a table of tables where $[a,b,c]$ is in seen table if $a$
in $seen$ and $b$ in $seen[a]$ and $c$ in $seen[a][b]$. To add to seen
table add element wise from $a$ first then to $c$

# Best Time to Buy and Sell Stock

## Link

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Where

Leetcode

## Difficulty

Easy

## Description

You are given an array prices where prices\[i\] is the price of a given
stock on the ith day. You want to maximize your profit by choosing a
single day to buy one stock and choosing a different day in the future
to sell that stock. Return the maximum profit you can achieve from this
transaction. If you cannot achieve any profit, return 0.

## Solution Main Idea

Keep a pointer for low and high. If price\[low\] \< price\[high\] then
check if its more than maxProfit. In either case move high pointer to
the right. Else if price\[low\] \> price\[high\] then set low pointer to
equal high pointer and move high pointer to the right. Do this while
both pointers are in range. Report highest profit

# climbing-stairs

## Link

https://leetcode.com/problems/climbing-stairs/

## Where

Leetcode

## Difficulty

Easy

## Description

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?

## Solution Main Idea

Use DP. Let $totalSteps[i]$ denote the num of distinct ways to reach the
top when you're at step $i$. step 0 indicates that you're not on the
stairs yet. step $n$ indicates you're at the top.

Fill in $totalSteps$ from $n$ to $0$.
$totalSteps[i] = totalSteps[i+1] + totalSteps[i+2]$

# Clone Graph

## Link

https://leetcode.com/problems/clone-graph/

## Where

Leetcode

## Difficulty

Medium

## Description

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List\[Node\])
of its neighbors.

class Node { public int val; public List`<Node>`{=html} neighbors; }

Test case format:

For simplicity, each node's value is the same as the node's index
(1-indexed). For example, the first node with val == 1, the second node
with val == 2, and so on. The graph is represented in the test case
using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a
finite graph. Each list describes the set of neighbors of a node in the
graph.

The given node will always be the first node with val = 1. You must
return the copy of the given node as a reference to the cloned graph.

## Solution Main Idea

Use DFS. Have a dictionary where key is the node val and value is the
node. For each neighbor, first check that it is in the mapper, if it is
then add from the map to the cloned neighbor array. If not then create a
new node through DFS. DFS returns the cloned node.

Space is $O(V)$ since each each node is stored in memory only once. All
neighbors of a node are pointers to an entry in the mapper in memory.

# Coin Change

## Link

https://leetcode.com/problems/coin-change/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of
money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the
coins, return -1.

You may assume that you have an infinite number of each kind of coin.

## Solution Main Idea

DP. Let A\[i\] denote the least amount of coins needed to fulfill amount
$i$. $A[i] = min(A[i], 1+A[i-coin])$ Let $A[i]$ be the minimum of using
that coin or not using that coin.

# Combination Sum 4

## Link

https://leetcode.com/problems/combination-sum-iv/submissions/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an array of distinct integers nums and a target integer target,
return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit
integer.

## Solution Main Idea

Use DP. Let A\[i\] be the number of permutations to reach $i$. For each
$i$, go through each num in nums, such that $A[i] = A[i - num] + A[i]$
(We take it or not)

# Contains Duplicate

## Link

https://leetcode.com/problems/contains-duplicate/

## Where

Leetcode

## Difficulty

Easy

## Description

Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.

## Solution Main Idea

Keep dictionary of num frequency, find values in dictionary with
frequency $\geq$ 2

# Decode Ways

## Link

https://leetcode.com/problems/decode-ways/

## Where

Leetcode

## Difficulty

Medium

## Description

A message containing letters from A-Z can be encoded into numbers using
the following mapping:

'A' -\> "1" 'B' -\> "2" ... 'Z' -\> "26" To decode an encoded message,
all the digits must be grouped then mapped back into letters using the
reverse of the mapping above (there may be multiple ways). For example,
"11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6) "KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be
mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to
decode it.

The test cases are generated so that the answer fits in a 32-bit
integer.

## Solution Main Idea

Use DP. Similar to work-break. Let $A[i]$ represent the number of ways
to decode in suffix $s[i:]$. For each $s[i:]$, find all mappings that
matches the prefix of $s[i:]$, and add up the number of ways to decode
all suffixes that have the prefix removed.

$A[i] += A[i + len(match)]$

# Find Minimum in Rotated Sorted Array

## Link

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## Where

Leetcode

## Difficulty

Medium

## Description

Suppose an array of length n sorted in ascending order is rotated
between 1 and n times. For example, the array nums = \[0,1,2,4,5,6,7\]
might become:

\[4,5,6,7,0,1,2\] if it was rotated 4 times. \[0,1,2,4,5,6,7\] if it was
rotated 7 times. Notice that rotating an array \[a\[0\], a\[1\], a\[2\],
..., a\[n-1\]\] 1 time results in the array \[a\[n-1\], a\[0\], a\[1\],
a\[2\], ..., a\[n-2\]\].

Given the sorted rotated array nums of unique elements, return the
minimum element of this array.

You must write an algorithm that runs in O(log n) time.

## Solution Main Idea

Divide and conquer using binary search. An inflection point is defined
to be between $i$ and $i+1$ where $A[i-1] < A[i] > A[i+1]$. $A[i]$ would
be the biggest element in nums, and $A[i+1]$ would be the smallest.

All the elements to the left of inflection point \> first element of the
array. All the elements to the right of inflection point \< first
element of the array.

4 5 6 7 2 3

1.  Find the mid element of the array.

2.  If mid element \> first element of array this means that we need to
    look for the inflection point on the right of mid.

3.  If mid element \< first element of array this that we need to look
    for the inflection point on the left of mid.

# House Robber

## Link

https://leetcode.com/problems/house-robber/

## Where

Leetcode

## Difficulty

Medium

## Description

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security systems connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each
house, return the maximum amount of money you can rob tonight without
alerting the police.

## Solution Main Idea

Use DP. Let $A[i]$ be the maximum amount of money you can steal from
houses in $nums[0:i]$ (subarray of $nums$ ending at $i$).

$A[i] = max(nums[i] + A[i-2] \text{(include if i - 2 >=0)}, A[i - 1])$
(Steal from $i$ or not). Return $A[len(nums)-1]$

# House Robber 2

## Link

https://leetcode.com/problems/house-robber-ii/

## Where

Leetcode

## Difficulty

Medium

## Description

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this
place are arranged in a circle. That means the first house is the
neighbor of the last one. Meanwhile, adjacent houses have a security
system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each
house, return the maximum amount of money you can rob tonight without
alerting the police.

## Solution Main Idea

Just use house-robber twice. Once without the first element, once
without the last. Return the max of the two

# Jump Game

## Link

https://leetcode.com/problems/jump-game/submissions/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given an integer array nums. You are initially positioned at the
array's first index, and each element in the array represents your
maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

## Solution Main Idea

Use DP. Let $A[i]$ represent the furthest one could reach by jumping
through a particular subsequence in $nums[0:i]$ that ends at $i$. If
$A[i-1] >= i$, meaning we can jump to $i$, then
$A[i] = max(A[i-1], i + nums[i])$. (If we jump from $i$, then the
furthest we can go from $i$ is $i + nums[i]$, if we don't jump from $i$,
then in order to proceed we must jump from somewhere before $i$, and
furthest we could jump from before $i$ is $A[i-1]$.)

# Longest Increasing Subsequence

## Link

https://leetcode.com/problems/longest-increasing-subsequence/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by
deleting some or no elements without changing the order of the remaining
elements. For example, \[3,6,2,7\] is a subsequence of the array
\[0,3,1,6,2,2,7\].

## Solution Main Idea

Let $A[i]$ denote the LIS that ends at index $i$.

$$A[i] = max(A[j]+1: j<i, A[j]<A[i])$$

max over all $A[i]$'s

Base case: all $A[i]$'s = 1

# Maximum Product Subarray

## Link

https://leetcode.com/problems/maximum-product-subarray/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an integer array nums, find a contiguous non-empty subarray within
the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit
integer.

A subarray is a contiguous subsequence of the array.

## Solution Main Idea

Similar to maximum-subarray problem. DP. Let local_max\[i\] denote the
largest product among all subarrays of $nums$ that end at index i.
local_max\[i\] denote the smallest product among all subarrays of $nums$
that end at index i. If $nums[i]$ is negative, then what was local max
in the previous i might very well be the smallest in this i. What was
local min in the previous i might be the biggest in this i. We also have
to consider $num[i]$ on its own as well

# Maximum Subarray

## Link

https://leetcode.com/problems/maximum-subarray/submissions/

## Where

Leetcode

## Difficulty

Easy

## Description

Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

## Solution Main Idea

![Intuition](maximum-subarray.png)

DP. Let local_max\[i\] be the biggest sum out of all possible subarrays
that end at index i.

local_max\[i\] = max(nums\[i\], local_max\[i-1\] + nums\[i\])

in other words

local_max = max(nums\[i\], local_max + nums\[i\])

Get max of all local_max\[i\]'s to obtain answer

# product-of-array-except-self

## Link

https://leetcode.com/problems/product-of-array-except-self/

## Where

Leetcode

## Difficulty

Easy

## Description

Given an integer array $nums$, return an array $answer$ such that
$answer[i]$ is equal to the product of all the elements of $nums$ except
$nums[i]$.

The product of any prefix or suffix of $nums$ is guaranteed to fit in a
32-bit integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

## Solution Main Idea

Keep track of a suffix and prefix array. Prefix\[i\] = product of the
prefix of num bounded by i excluding i. Suffix\[i\] = product of suffix
of num bounded by i excluding i. $answer[i] = prefix[i] = suffix[i]$

# Unique Paths

## Link

https://leetcode.com/problems/unique-paths/

## Where

Leetcode

## Difficulty

Medium

## Description

There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid\[0\]\[0\]). The robot tries to move to the
bottom-right corner (i.e., grid\[m - 1\]\[n - 1\]). The robot can only
move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique
paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or
equal to 2 \* 109.

## Solution Main Idea

Use DP. Let $A[i][j]$ represent the number of ways to reach row $i$ col
$j$. $A[i][j] = A[i-1][j] + A[i][j-1]$. Return $A[n-1][m-1]$

# Word Break

## Link

https://leetcode.com/problems/word-break/submissions/

## Where

Leetcode

## Difficulty

Medium

## Description

Given a string s and a dictionary of strings wordDict, return true if s
can be segmented into a space-separated sequence of one or more
dictionary words.

Note that the same word in the dictionary may be reused multiple times
in the segmentation.

## Solution Main Idea

Use DP. let $A[i]$ represent whether or not we can express suffix
$s[i:]$ as a combination of wordDict. For each word $matchingPrefix$
that matches the prefix of the suffix $s[i:]$,
$A[i] = A[i+len(matchingPrefix)] or A[i]$ (We use it or dont use it).
Return $A[0]$

Or

Use BFS. Let $s$ be a vertex such that $vertices[s]$ is a string. Get
all possible words in wordDict that is a prefix of $vertices[s]$ and set
the suffix of $vertices[s]$ excluding them as adjacent to $vertices[s]$.
Let $vertices[""]$ be the vertex we wish to visit. Run BFS from
$vertices[s]$ and return true if we visit $vertices[""]$. Else false.
