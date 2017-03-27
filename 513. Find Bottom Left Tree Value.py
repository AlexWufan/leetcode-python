# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # level-order traversal. right to left.
        queue = [root]
        while queue:
        	root = queue.pop(0)
        	res = root.val
        	if root.right:
        		queue.append(root.right)
        	if root.left:
        		queue.append(root.left)
        return res

        # better
	def findLeftMostNode(self, root):
	    queue = [root]
	    for node in queue:
	        queue += filter(None, (node.right, node.left))
	    return node.val     
	    
	    #递归
class Solution(object):
	def findBottomLeftValue(self, root):
		self.res = 0
		self.h = 0
		self.findleft(root,1)
		return self.res
	def findleft(self, root, depth):
		if self.h < depth:
			self.h = depth
			self.res = root.val
		if root.left:
			self.findleft(root.left,depth+1)
		if root.right:
			self.findleft(root.right,depth+1)