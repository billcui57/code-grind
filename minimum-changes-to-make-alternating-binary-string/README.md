# Minimum Changes To Make Alternating Binary String

## Link
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

## Where
Leetcode

## Difficulty
Easy

## Description
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

## Solution Main Idea
Small observation that the sequence of index is [0,1,2,3..],
if we get its module by 2, we get [0,1,0,1,0..],
which is the alternating binary sequence we want.

So we iterate the string,
check if the characters[i] is same as the i % 2.
Note that s[i] is a character,
and s[i] - '0' making it to integer.

We accumulate the number of difference,
which is the number of operation to make it into 01 string.

We can do the same to find out res,
the number of operation for 10 string.
But we don't have to,
becaue this equals to s.length - res.

