# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = set()
        self.helper(root,res)
        return sorted(res)[1] if len(res)>1 else -1
        
    def helper(self, node, res):
        if not node:
            return None
        res.add(node.val)
        self.helper(node.left,res)
        self.helper(node.right,res)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min1 = root.val
        self.res = float('inf')
        
        def helper(node):
            if not node:
                return None
            if node.val != min1:
                self.res = min(node.val, self.res)
            helper(node.left)
            helper(node.right)

        helper(root)
        return self.res if self.res!=float('inf') else -1
        