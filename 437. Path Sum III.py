# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
        	return 0
        ans = 0
        ans += self.findPath(root,sum) + self.pathSum(root.left,sum) + self.pathSum(root.right,sum)
        return ans


    def findPath(self, root, sum):
    	if not root:
    		return 0
    	res = 0
    	if root.val == sum:
    		res += 1
    	res+=self.findPath(root.left,sum-root.val)
    	res+=self.findPath(root.right,sum-root.val)
    	return res


#O(N)时间复杂度算法，用hash table
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return 0
        dic = {0:1}
        so_far = 0
        return self.findPath(root, s, so_far, dic)


    def findPath(self, root, s, so_far, dic):
        if not root:
            return 0
        so_far += root.val
        res = dic.get(so_far-s, 0)
        dic[so_far]=dic.get(so_far, 0)+1
        res += self.findPath(root.left, s, so_far, dic)
        res += self.findPath(root.right, s, so_far, dic)
        dic[so_far]-=1
        return res