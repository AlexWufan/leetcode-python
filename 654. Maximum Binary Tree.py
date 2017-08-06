# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        root = TreeNode(max(nums))
        index = nums.index(max(nums))
        left = nums[:index] if index >= 1 else []
        right = nums[index+1:] if index + 1 < len(nums) else []
        root.left =  self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root