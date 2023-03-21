# Minimum Deletions to Make Character Frequencies Unique

## Link
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/

## Where
Leetcode

## Difficulty
Medium

## Description
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

## Solution Main Idea
Get freq, only care about freq. Make sure freq are unique by using set and counting number of times we need to dec freq to be unique