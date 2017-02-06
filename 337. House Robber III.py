# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.DFShelper(root))
        # return self.DFShelper(root)[1]
    def DFShelper(self, root):
    	if root is None:
    		return (0,0)
    	left = self.DFShelper(root.left)
    	right = self.DFShelper(root.right)
    	return (left[1]+right[1], max(left[0]+right[0]+root.val, left[1]+right[1]))