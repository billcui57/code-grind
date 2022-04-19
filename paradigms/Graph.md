# Detecting Cycles

## Undirected

Use either disjoint set data structure or use DFS. For DFS, if an adjacent non-originating vertex is visited then there is a cycle.

## Directed

Perform topological sort $O(n+m)$. Topological sort exists iff DAG. We cannot use the same approach as we did in undirected graphs because directed cycles only exists if there are backedges (we are about to visit a node we have traversed from).

# Shortest Path

Given $s$, find shortest $s-v$ path for all $v$

## No Cycles

### Directed

Given $s$, find shortest $s-v$ path for all $v$

Use topological sort, then use DP.

Use topological sort to find vertex order $1,2,...,n$ so every directed edge $(i,j)$ has $i$ appear before $j$ in list.

Any vertex $v$ that appears before $s$ in list will not have a path from $s$ to $v$, so we can discard then from list. Now $s$ will be the first element$

Let $A[i]$ be the distance from $s$ to the vertex at index $i$, $n$ be the length of the list after discarding

      A[i] = infty for all i
      A[0] = 0
      for i in 0...n:
        for every edge (vertex at index i, vertex at index j):
          A[i] = min(A[i], A[j] + weight(vertex at index i, vertex at index  j))

### Undirected

Its a tree, the shortest path is the only path

## No negative weights

Dijkstras

## Allow negative weights and allow cycles but no negative weight cycles

Bellman-Ford

## All shortest paths - no negative weight cycles

Floyd-Warshall
