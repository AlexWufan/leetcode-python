# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        self.dfs(root,[0])
        return root

    def dfs(self, root, tmp):
        if not root:return None

        self.dfs(root.right, tmp)

        root.val += tmp[0]
        tmp[0] = root.val

        self.dfs(root.left, tmp)
        return root