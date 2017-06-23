# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not (s and t): return s is t
        if self.isSameTree(s,t): return True
        else:
            return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return (p is q) or bool(p and q) and p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)