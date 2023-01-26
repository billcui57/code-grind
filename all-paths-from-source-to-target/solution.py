class Solution:

    def DFS(self, node, graph, seen, buffer, result):

        buffer.append(node)
        if node == len(graph)-1:
            result.append(copy.deepcopy(buffer))
            buffer.pop()
            return

        seen.add(node)

        neighbours = graph[node]

        for neighbour in neighbours:
            if neighbour not in seen:
                self.DFS(neighbour, graph, seen,buffer,result)

        seen.remove(node)
        buffer.pop()


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []

        self.DFS(0, graph, set(), [], result)
        return result
