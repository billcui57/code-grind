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


## Code

```python
class Solution:

    def createAdj(self, prereqs, numCourses):
        
        adj = dict()
        for node in range(numCourses):
            adj[node] = []


        for prereq in prereqs:
            before, after = prereq
            adj[before].append(after)
        return adj

    def dfs(self,node, adj, seen, visited,unvisited,result):
        
        if node in seen:
            raise Exception("not a DAG")
        if node in visited:
            return

        seen.add(node)
        unvisited.remove(node)
        visited.add(node)
        
        neighbours = adj[node]
        for neighbour in neighbours:
            self.dfs(neighbour, adj, seen, visited, unvisited, result)
        
        seen.remove(node)
        result.append(node)
        


    def topologicalSort(self, adj):
        unvisited = set(adj.keys())
        visited = set()
        result = []
        print(unvisited)
        try:
            while len(unvisited) >0:
                node = next(iter(unvisited))
                self.dfs(node,adj,set(),visited, unvisited, result)
        except Exception as e:
            print("err:",e)
            return False
        print(result)
        return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = self.createAdj(prerequisites, numCourses)
        return self.topologicalSort(adj)
```
