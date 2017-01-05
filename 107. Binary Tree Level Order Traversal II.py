# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, level = [], [root]
        while root and level:
        	res.append([node.val for node in level])
        	level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res[::-1]


        #栈的实现

        res = []
        stack = [(root, 0)]
        while stack:
        	node, level = stack.pop()
        	if node:
        		if len(res) < level+1:
        			res.insert(0, [])
        		res[-(level+1)].append(node.val)
        		stack.append((node.right, level+1))
        		stack.append((node.left, level+1))
        return res