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



        