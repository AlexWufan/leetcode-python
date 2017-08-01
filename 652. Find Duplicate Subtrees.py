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
        if not root:
            return None
        res = []
        allnode = []
        stack = [root]
        while stack:
            node = stack.pop()
            allnode.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        for i in range(len(allnode)):
            for j in range(len(allnode)):
                if i != j and self.isSameTree(allnode[i],allnode[j]) and not allnode[i] in res and not allnode[j] in res:
                    res.append(allnode[i])
        return res
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return (p is q) or bool(p and q) and p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)