# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.postorder(res,root)
        return res[0]
    
    def postorder(self,res,root):
        if not root:return 0
        left = self.postorder(res, root.left)
        right = self.postorder(res, root.right)
        res[0] +=bas(left-right)
        return root.val + left + right
    