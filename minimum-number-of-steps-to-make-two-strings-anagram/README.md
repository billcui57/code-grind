# Minimum Number of Steps to Make Two Strings Anagram

## Link

https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

## Solution Main Idea

Count delta of char freq. Divide by 2. Delta is always divisible by 2 because if a char is missing in one string at location i. Then a different char must be in that string somewhere that does not exist as frequently in the other string to take its place.
