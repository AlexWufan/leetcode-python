# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root,float('-inf'),float('inf'))
    
    def isValid(self, node, minimum, maximum):   
        if not node:
    		return True
    	if node.val < minimum and node.val > maximum:
    		return False
    	return self.isValid(node.left, minimum, node.val) and self.isValid(node.right,node.val, maximum)



# 还有一种是遍历。遍历一遍然后排序







# from discuss. Very short
	def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
	    if not root: 
	        return True
	    if root.val <= floor or root.val >= ceiling:
	        return False
	    # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
	    return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)