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
