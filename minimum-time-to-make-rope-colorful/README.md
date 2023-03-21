# Minimum Time to Make Rope Colorful

## Link
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

## Where
Leetcode

## Difficulty
Medium

## Description
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

## Solution Main Idea
The minimize time depends on whether if we are cutting the left string or the right string when we encounter two consecutive balloons of the same colour. Just pick the one that takes the least amount of time, and set the colour and the index of that last colour that we have seen to be the index of the string we did not cut. Effectively ignoring the cut string from future considerations

