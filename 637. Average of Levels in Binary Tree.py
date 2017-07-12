# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ave = []
        level = [root]
        while level:
            ave.append(sum(node.val for node in level)/len(level))
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return ave