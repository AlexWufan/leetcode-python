# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        res = 0
        if root.left:
            if root.left.left is None and root.left.right is None:
                res += root.left.val
            else:
                res += self.sumOfLeftLeaves(root.left)
        res += self.sumOfLeftLeaves(root.right)
        return res


#more compact,leetcode discuss
class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root: return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)   # isn't leave


#DFS using stack
	def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        stack = [root]
        res = 0
        while stack:
        	node = stack.pop()
        	if node.left:
        	    if not node.left.left and not node.left.right:
        		res+=node.left.val
        	    else:
        		stack.append(node.left)
        	if node.right:
        		stack.append(node.right)
        return res
        
#BFS using queue
	def sumOfLeftLeaves(self, root):
	        """
	        :type root: TreeNode
	        :rtype: int
	        """
	        if not root: return 0
	        stack = [root]
	        res = 0
	        while stack:
	        	node = stack.pop(0)
	        	if node.left:
	        	    if not node.left.left and not node.left.right:
	        		res+=node.left.val
	        	    else:
	        		stack.append(node.left)
	        	if node.right:
	        		stack.append(node.right)
	        return res
