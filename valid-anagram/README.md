# Valid Anagram

## Link

https://leetcode.com/problems/valid-anagram/submissions/

## Where

Leetcode

## Difficulty

Easy

## Description

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Solution Main Idea

Build freqDict from $s$, decrease from freqDict with characters in $t$. Return True if freqDict is all zeros.
