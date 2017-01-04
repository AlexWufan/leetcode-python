# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        stack = []
        while stack or root:
        	if root:
        		stack.append(root)
        		root = root.left
        	else:
        		node = stack.pop()
        		res.append(node.val)
        		root = node.right
        return res[k-1]
