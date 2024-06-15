# Maximal Network Rank

## Link
https://leetcode.com/problems/maximal-network-rank/description/

## Where
Leetcode

## Difficulty
Medium

## Description
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

## Solution Main Idea
Get adj, obtain deg of all cities. Iterate through all pairs and return largest sum. O(n^2)


## Code

```python
class Solution:
    def get_adj(self,roads):
        adj = dict()

        for road in roads:
            a = road[0]
            b = road[1]
            if a not in adj:
                adj[a] = set([b])
            else:
                adj[a].add(b)
            if b not in adj:
                adj[b] = set([a])
            else:
                adj[b].add(a)
        return adj

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        adj = self.get_adj(roads)
        print(adj)

        maxCity = 0


        # iterate through all pairs and find the max return
        
```
