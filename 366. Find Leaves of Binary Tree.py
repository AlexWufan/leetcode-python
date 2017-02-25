# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, root,res):
        if not root:
            return 0
        h = 1 + max(self.helper(root.left, res), self.helper(root.right, res))
        if len(res) < h:
            res.append([])
        res[h-1].append(root.val)
        root.left, root.right = None, None
        return h
        