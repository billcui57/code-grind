# Detecting Cycles

## Undirected

Use either disjoint set data structure or use DFS. For DFS, if an adjacent non-originating vertex is visited then there is a cycle.

## Directed

Perform topological sort. Topological sort exists iff DAG. We cannot use the same approach as we did in undirected graphs because directed cycles only exists if there are backedges (we are about to visit a node we have traversed from).
