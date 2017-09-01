# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dic = {}
        res = 0
        self.dfs(root,1,1)
        for x in self.dic:
            res = max(res, self.dic[x][-1] - self.dic[x][0] + 1)
        return res
    
    def dfs(self, root, dep, index):
        if not root:return None
        if dep not in self.dic:
            self.dic[dep] = []
        self.dic[dep].append(index)
        print(self.dic)
        self.dfs(root.left, dep+1, index*2)
        self.dfs(root.right, dep+1, index*2 +1)
        