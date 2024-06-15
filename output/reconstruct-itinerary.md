# Reconstruct Itinerary

## Link

https://leetcode.com/problems/reconstruct-itinerary/description/

## Where

Leetcode

## Difficulty

Hard

## Description

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

## Solution Main Idea

Create adj list, modify list as you DFS to ensure you only traverse an edge once. Restore that edge once youre done DFS'ing.
Sort the neighbours lexicalgraphically. Return first result that uses all edges.


## Code

```python
class Solution:

    def DFS(self, node, adj,adjCount,buffer,result):
        
        buffer.append(node)
        if adjCount == 0:
            result.append(buffer)
            return True

        neighbours = adj[node] if node in adj else []
        

        for i in range(len(neighbours)):
            if neighbours[i] == "-":
                continue
            store = neighbours[i]
            neighbours[i] = "-"
            adjCount-=1
            found = self.DFS(store, adj,adjCount, buffer, result)
            if found:
                return found #early return
            neighbours[i] = store
            adjCount+=1
            
        buffer.pop()
        return False
    def getAdj(self, tickets):
        adj = dict()
        adjCount = 0
        for ticket in tickets:
            fromLoc,toLoc = ticket[0], ticket[1]
            if fromLoc not in adj:
                adj[fromLoc] = [toLoc]
            else:
                adj[fromLoc].append(toLoc)
            adjCount += 1
        for fromLoc in adj.keys():
            adj[fromLoc] = list(sorted(adj[fromLoc]))
        return adj, adjCount
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj,adjCount = self.getAdj(tickets)
        # print(adj)
        results = []
        self.DFS("JFK",adj,adjCount,[],results)
        best_result = results[0]
        return best_result

```
