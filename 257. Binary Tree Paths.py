# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
    	if not root:
    		return []
    	res, stack =[], [[root, str(root.val)]]
    	while stack:
    		node, path = stack.pop()
    		if not node.left and not node.right:
    			res.append(path)
    		if node.right:
    			stack.append([node.right, path + '->' + str(node.right.val)])
    		if node.left:
    			stack.append([node.left, path + '->' + str(node.left.val)])
    	# modify res to string 
    	return res

# BFS
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
    	if not root:
    		return []
    	res, queue =[], [[root, str(root.val)]]
    	while queue:
    		node, path = queue.pop(0)
    		if not node.left and not node.right:
    			res.append(path)
    		if node.right:
    			queue.append([node.right, path + '->' + str(node.right.val)])
    		if node.left:
    			queue.append([node.left, path + '->' + str(node.left.val)])
    	return res

# recursive
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
    	if not root:
    		return []
    	res = []
    	self.DFS(root,str(root.val),res)
    	return res

    def DFS(self,node,path,res):
    	if not node.left and not node.right:
    		res.append(path)
    	if node.right:
    		self.DFS(node.right, path + '->' + str(node.right.val), res)
    	if node.left:
    		self.DFS(node.left, path + '->' + str(node.left.val), res)





# stefan的解法，非常简洁
	# def binaryTreePaths(self, root):
	#     if not root:
	#         return []
	#     return [str(root.val) + '->' + path
	#             for kid in (root.left, root.right) if kid
	#             for path in self.binaryTreePaths(kid)] or [str(root.val)]