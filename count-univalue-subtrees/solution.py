# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, result):
        if node is None:
            return False, None

        if node.left is None and node.right is None:
            result[0] += 1
            return True, node.val
        
        leftUni = False
        rightUni = False
        leftVal = None
        rightVal = None
        if node.left:
            leftUni,leftVal = self.helper(node.left,result)
        if node.right:
            rightUni, rightVal = self.helper(node.right,result)
        
        if (not node.left or (leftUni and leftVal == node.val)) and (not node.right or (rightUni and rightVal == node.val)):
            result[0]+=1
            return True, node.val
        return False, node.val
        

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        result = [0]
        self.helper(root, result)
        return result[0]
