"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def helper(self,node,seen,result):
        if node.val in seen:
            result.append(node)
            return
        seen.add(node.val)
        if node.parent is not None:
            self.helper(node.parent, seen,result)

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen =set()
        result = []
        self.helper(p, seen, result)
        self.helper(q,seen,result)
        return result.pop()