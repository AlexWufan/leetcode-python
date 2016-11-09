# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path, res = [], []
        self.findPath(root, sum, path, res)
        return res

# actually DFS
    def findPath(self, root, sum, path, res):
        if root is None:
        	return 
        if not root.left and not root.right and root.val == sum:
        	path.append(root.val)
        	res.append(path)
        self.findPath(root.left, sum-root.val, path+[root.val], res)
        self.findPath(root.right, sum-root.val, path+[root.val], res)




# 还可以计算出每一条路径的和，再筛选，但是还是不明白如何存储的？
	def pathSum(self, root, sum):
	    if not root:
	        return []
	    if not root.left and not root.right and sum == root.val:
	        return [[root.val]]
	    tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
	    return [[root.val]+i for i in tmp]

