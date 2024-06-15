# Remove Max Number of Edges to Keep Graph Fully Traversable

## Link
https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/

## Where
Leetcode

## Difficulty
Hard

## Description
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

## Solution Main Idea
Union find. Two sets. Sets of node that alice and bob can visit. Go through type 3 edges first. Start with no edges, and add edges.
Add 1 if union does thing.


## Code

```python
class UnionFind:

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node]) #cache
            return self.parents[node]
        return node
    
    def union(self, node1, node2):
        find1 = self.find(node1)
        find2 =self.find(node2)
        if find1 == find2:
            return False

        if find1 < find2:
            self.parents[find2] = find1
        else:
            self.parents[find1] = find2
        self.numDisjoint -=1
        return True
    
    def connected(self):
        # print(self.numDisjoint)
        return self.numDisjoint == 1

    def __init__(self,numNodes):
        self.parents = [i for i in range(numNodes)]
        self.numDisjoint = numNodes
        


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        aliceUnion = UnionFind(n)
        bobUnion = UnionFind(n)
        numEdges = 0

        edges = [[edge[0],edge[1]-1,edge[2]-1] for edge in edges]
        type3 = filter(lambda x: x[0] == 3, edges)
        type2 = filter(lambda x: x[0] == 2, edges)
        type1 = filter(lambda x: x[0] == 1, edges)
       

        for edge in type3:
            [etype, u,v] = edge
            addEdge = False
            if aliceUnion.union(u,v):
                addEdge = True
            if bobUnion.union(u,v):
                addEdge = True
            if addEdge:
                numEdges += 1
        
        for edge in type2:
            [etype, u,v] = edge
            if bobUnion.union(u,v):
                numEdges +=1

        for edge in type1:
            [etype, u,v] = edge
            if aliceUnion.union(u,v):
                numEdges +=1 

        if aliceUnion.connected() and bobUnion.connected():
            return len(edges) - numEdges
        return -1



        
```
