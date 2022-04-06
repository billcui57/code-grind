class Solution:

    def getAdj(self, numCourses, prereqs):
        adj = {}

        for i in range(numCourses):
            adj[i] = []

        for i in range(len(prereqs)):
            start = prereqs[i][1]
            end = prereqs[i][0]
            adj[start].append(end)

        return adj

    def DFS(self, adj, node, permanent, nonPermanent, temp, top):

        if node in temp:
            raise Exception('not DAG')
        if node in permanent:
            return

        temp.add(node)

        for child in adj[node]:
            self.DFS(adj, child, permanent, nonPermanent, temp, top)

        temp.remove(node)
        permanent.add(node)
        nonPermanent.remove(node)
        top.append(node)

    def topologicalSort(self, adj, numCourses):
        nonPermanent = set(list(range(numCourses)))
        permanent = set()
        temp = set()
        top = []

        while len(nonPermanent) > 0:
            node = next(iter(nonPermanent))
            self.DFS(adj, node, permanent, nonPermanent, temp, top)

        return top

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = self.getAdj(numCourses, prerequisites)
        print(adj)
        try:
            self.topologicalSort(adj, numCourses)
            return True
        except Exception as e:
            return False
