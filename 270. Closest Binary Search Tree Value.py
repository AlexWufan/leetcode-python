# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:return None
        distance = [float('inf'), root.val]
        self.inorder(root, target, distance)
        return distance[1]
    
    def inorder(self, root, target, distance):
        if not root:return None
        self.inorder(root.left, target, distance)
        if abs(target - root.val) < distance[0]:
            distance[0] = abs(root.val - target)
            distance[1] = root.val
        # 下面这样写是错的,python的可变类型与不可变类型！
            distance = [abs(root.val - target), root.val]
        self.inorder(root.right, target, distance)

# 下面的效率好
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:return None
        res = root.val
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            if target<root.val:
                root = root.left
            else:
                root = root.right
        return res