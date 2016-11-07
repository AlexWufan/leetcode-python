# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
    	if not root:
    		return []
    	res = [], path = [root.val], stack = [root]
    	while stack:
    		node = stack.pop()
    		if not node.left and not node.right:
    			res.append(path)
    			path.pop()
    		if node.left:
    			stack.append(node.left)
    			path.append(node.left.val)
    		if node.right:
    			stack.append(node.right)
    			path.append(node.right.val)
    	# modify res to string 
    	return res













# stefan的解法，非常简洁
	# def binaryTreePaths(self, root):
	#     if not root:
	#         return []
	#     return [str(root.val) + '->' + path
	#             for kid in (root.left, root.right) if kid
	#             for path in self.binaryTreePaths(kid)] or [str(root.val)]