# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.maxDepth(root,res)
        return res[0]
        
    
    def maxDepth(self,root,res):
        if not root:
            return 0
        left = self.maxDepth(root.left,res)
        right = self.maxDepth(root.right,res)
        res[0] = max(res[0], left+right)
        return max(left,right)+1