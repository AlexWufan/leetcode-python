# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        if root.val <= p.val:
        	return self.inorderSuccessor(root.right, p)
        else:
        	left = self.inorderSuccessor(root.left, p)
        	return left if left else root

# 上面是递归，不太好理解。
# 下面是迭代。

	def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ
