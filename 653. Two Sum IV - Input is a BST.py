# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        dic = set()
        self.dfs(root,dic)
        for node in dic:
            if k-node in dic and k-node != node:
                return True
        return False
    
    def dfs(self, root, dic):
        if not root:
            return None
        self.dfs(root.left, dic)
        dic.add(root.val) 
        self.dfs(root.right, dic)