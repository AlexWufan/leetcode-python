# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
        	return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) and p.val == q.val
        else: 
        	return p is q

# 一行
		return p is q or p and q and p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)