# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:return None
        if t1 and t2: 
            val = t1.val+t2.val
            left1 = t1.left
            left2 = t2.left
            right1 = t1.right
            right2 = t2.right
        elif t1 and not t2:
            val = t1.val
            left1 = t1.left
            left2 = None
            right1 = t1.right
            right2 = None
        else:
            val = t2.val
            left1 = None
            left2 = t2.left
            right1 = None
            right2 = t2.right
        
        root = TreeNode(val)
        root.left = self.mergeTrees(left1,left2)
        root.right = self.mergeTrees(right1,right2)
        return root



class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2