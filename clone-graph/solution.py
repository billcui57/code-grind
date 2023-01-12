"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:

    def clone(self, node, mapping):
        if node is None:
            return None

        clonedNode = Node(val = node.val)
        mapping[node.val] = clonedNode

        for neighbour in node.neighbors:
            clonedNeighbour = None
            if neighbour.val in mapping:
                clonedNeighbour = mapping[neighbour.val]
            else:
                clonedNeighbour = self.clone(neighbour,mapping)
            clonedNode.neighbors.append(clonedNeighbour)
        return clonedNode

    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.clone(node,{})

# bfs version
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def cloneGraph(self, givenNode: 'Node') -> 'Node':
        if givenNode is None:
            return None

        madeNodes = dict()

        seen = set()
        queue = []

        queue.append(givenNode)
        seen.add(givenNode.val)

        madeNodes[givenNode.val] = Node(val = givenNode.val)

        while len(queue) > 0:

            node = queue.pop(0)
            newNode = madeNodes[node.val]
            
            for neighbour in node.neighbors:
                
                newNeighbourNode = None
                if neighbour.val in madeNodes:
                    newNeighbourNode = madeNodes[neighbour.val]
                else:
                    newNeighbourNode = Node(val = neighbour.val)
                    madeNodes[neighbour.val] = newNeighbourNode
                newNode.neighbors.append(newNeighbourNode)

                if neighbour.val not in seen:
                    queue.append(neighbour)
                    seen.add(neighbour.val)
        return madeNodes[givenNode.val]


# or go to adj list and back

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def graphToAdj(self, node):
        adjList = dict()

        queue=[]
        seen = set()

        if node is None:
            return adjList
        
        queue.append(node)
        seen.add(node.val)

        while len(queue) > 0:
            node = queue.pop(0)
        
            adjList[node.val] = [neighbour.val for neighbour in node.neighbors]

            for neighbour in node.neighbors:
                if neighbour.val not in seen:
                    queue.append(neighbour)
                    seen.add(neighbour.val)
        return adjList
            
    def adjToGraph(self, adjList):
        nodes = dict()
        for nodeVal in adjList.keys():
            nodes[nodeVal] = Node(val = nodeVal)
        
        for nodeVal, neighbourVals in adjList.items():
            for neighbourVal in neighbourVals:
                nodes[nodeVal].neighbors.append(nodes[neighbourVal])
        
        return nodes


    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        graph= self.adjToGraph(self.graphToAdj(node))
        return graph[node.val]
        