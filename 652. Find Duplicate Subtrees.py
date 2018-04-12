# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        d = collections.defaultdict(list)
        def dfs(root):
            if not root: return 'None'
            string = str(root.val) + dfs(root.left) + dfs(root.right)
            d[string].append(root)
            return string
        dfs(root)
        return [nodes[0] for nodes in d.values() if nodes[1:]]