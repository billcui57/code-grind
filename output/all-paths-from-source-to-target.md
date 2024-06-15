# All Paths From Source to Target

## Link

https://leetcode.com/problems/all-paths-from-source-to-target/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

## Solution Main Idea

DFS while holding onto buffer. Flush buffer into result when reach end node. Can reuse same buffer by popping before returning


## Code

```python
class Solution:

    def DFS(self, node, graph, seen, buffer, result):

        buffer.append(node)
        if node == len(graph)-1:
            result.append(copy.deepcopy(buffer))
            buffer.pop()
            return

        seen.add(node)

        neighbours = graph[node]

        for neighbour in neighbours:
            if neighbour not in seen:
                self.DFS(neighbour, graph, seen,buffer,result)

        seen.remove(node)
        buffer.pop()


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []

        self.DFS(0, graph, set(), [], result)
        return result

```
