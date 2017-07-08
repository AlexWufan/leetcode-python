# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.inorder(root,res)
        return min(res[i+1]-res[i] for i in range(len(res)-1))
        
    def inorder(self, root, res):
        if root is None: return None
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)