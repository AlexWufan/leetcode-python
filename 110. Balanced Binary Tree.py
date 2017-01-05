# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.depth(root.left)-self.depth(root.right)) <= 1

    def depth(self, root):
    	if not root: return 0
    	return max(self.depth(root.left), self.depth(root.right))+1