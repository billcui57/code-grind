# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def preOrderTraversal(self, root, result):

        if root is None:
            result.append("N")
            return

        result.append(root.val)
        self.preOrderTraversal(root.left, result)
        self.preOrderTraversal(root.right, result)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        result = []

        self.preOrderTraversal(root, result)

        return ",".join([str(i) for i in result])

    def deezHelper(self, data):

        val = data.pop(0)

        if val == None:
            return None

        left = None
        right = None

        left = self.deezHelper(data)
        right = self.deezHelper(data)

        node = TreeNode(val)
        node.left = left
        node.right = right

        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = data.split(",")

        data = [None if d == "N" else int(d) for d in data]

        root = self.deezHelper(data)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
