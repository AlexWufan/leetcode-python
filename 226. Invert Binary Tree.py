# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
        	return None
        # 这里不用判断，or的话就是不交换空节点了
        # if root.right or root.left:

        root.right, root.left = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root



# recursively
	def invertTree1(self, root):
	    if root:
	        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
	        return root


# DFS	
	def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
		if not root: return None
		stack = []
		while stack:
			node = stack.pop()
			if node:
				node.right, node.left = node.left, node.right
				stack+=node.left,node.right
		return root

