# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        res = []
        self.helper(res, t)
        return ''.join(res)
    
    def helper(self, string, node):
        if not node:
            return None
        string += str(node.val)
        if node.left or node.right:
            string += '('
            self.helper(string, node.left)
            string += ')'

        if node.right:
            string += '('
            self.helper(string, node.right)
            string += ')'