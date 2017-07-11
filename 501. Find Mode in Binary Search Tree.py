# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:return []
        mode = {}
        self.preorder(root, mode)
        max_mode = max(mode.values())
        return [x for x,v in mode.items() if v == max_mode]

    def preorder(self, root, mode):
        if not root:
            return None
        mode[root.val] = mode.get(root.val,0) + 1
        self.preorder(root.left, mode)
        self.preorder(root.right, mode)