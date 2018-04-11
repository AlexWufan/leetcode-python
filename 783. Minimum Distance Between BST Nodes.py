# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.helper(root,res)
        return min([res[i]-res[i-1] for i in range(1,len(res))])        
        
    def helper(self, root, res):
        if root:
            self.helper(root.left,res)
            res.append(root.val)
            self.helper(root.right,res)