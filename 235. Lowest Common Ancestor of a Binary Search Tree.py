# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #还是不知道为什么错，
        '''
        if not root : return None
        path = [root]
        stack = [[root, path]]
        while stack:
        	node, path = stack.pop()
        	if node == p:
        		path1 = path
        	elif node == q:
        		path2 = path
        	if node.left:
        		stack.append([node.left, path.append(node.left)])
    		if node.right:
    			stack.append([node.right, path.append(node.right)])
    	for i in range(len(path1)):
    		if path1[i] == path2[i]:
    			continue
    		elif path[i] != path2[i]:
    			return path1[i-1]
    		else:
    			return path2[i+1]
    	'''

    	if not root: return None
    	if root.val > p.val and root.val > q.val:
    		return lowestCommonAncestor(root.left, p, q)
    	if root.val < p.val and root.val < q.val:
    		return lowestCommonAncestor(root.right, p, q)
    	else: return root





#stefan Solution
	def lowestCommonAncestor(self, root, p, q):
	    while (root.val - p.val) * (root.val - q.val) > 0:
	        root = (root.left, root.right)[p.val > root.val]
	    return root

	def lowestCommonAncestor(self, root, p, q):
    if p.val < root.val > q.val:
        return self.lowestCommonAncestor(root.left, p, q)
    if p.val > root.val < q.val:
        return self.lowestCommonAncestor(root.right, p, q)
    return root