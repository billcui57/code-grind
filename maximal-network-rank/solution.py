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
        