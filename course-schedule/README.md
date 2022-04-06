# Course Schedule

## Link

https://leetcode.com/problems/course-schedule/

## Where

Leetcode

## Difficulty

Medium

## Description

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

## Solution Main Idea

Determine if there is a topological sort. A topological sort exists in a graph iff it is a DAG (Directed Acyclic Graph). Can finish all courses iff it is a DAG.
