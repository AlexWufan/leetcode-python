# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#recursive solution
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res
    def helper(self, root, res):
    	if root:
    		res.append(root.val)
    		self.helper(root.left, res)
    		self.helper(root.right, res)




# iteratively


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        sres, stack = [], [root]
        while stack:
        	node = stack.pop()
        	res.append(node.val)
        	if node.right:
        		stack.append(node.right)
        	if node.left:
        		stack.append(node.left)
        	# or
        	# if node:
        	# 	stack.append(node.right)
        	# 	stack.append(node.left)
        	# 	res.append(node.val)
        return res