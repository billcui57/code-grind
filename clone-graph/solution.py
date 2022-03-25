"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:

    def DFS(self, node, mapping):

        mapping[node.val] = Node(node.val, [])

        for neighbor in node.neighbors:
            childNode = None
            if neighbor.val not in mapping:
                childNode = self.DFS(neighbor, mapping)
            else:
                childNode = mapping[neighbor.val]

            mapping[node.val].neighbors.append(childNode)

        return mapping[node.val]

    def cloneGraph(self, node: 'Node') -> 'Node':

        if node is None:
            return None

        return self.DFS(node, {})
