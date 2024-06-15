# Bus Routes

## Link

https://leetcode.com/problems/bus-routes/

## Where

Leetcode

## Difficulty

Hard

## Description

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

## Solution Main Idea

Use BFS.

To fulfill time constraint:

1. We do not want to go on the same bus more than once
2. We do not want to go to the same station more than once (dealt with by visited set)

To fulfill 1, our adjacency list should maintain info about each bus separately so that we can prune it from routes after we've used that bus route once


## Code

```python
class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        busesForStation = {}
        for i, route in enumerate(routes):
            for station in route:
                if station not in busesForStation:
                    busesForStation[station] = set()
                busesForStation[station].add(i)

        queue = []
        queue.append((source, 0))
        visited = set()
        for node, depth in queue:
            visited.add(node)
            if node == target:
                return depth
            for availableBus in busesForStation[node]:
                for station in routes[availableBus]:
                    if station not in visited:
                        queue.append((station, depth + 1))
                routes[availableBus] = []  # seen route, prune it
        return -1

```
