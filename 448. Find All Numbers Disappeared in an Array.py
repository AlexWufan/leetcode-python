class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            index = nums[i] - 1
            nums[index] = - nums[index]
        for i in range(len(nums)):
            res.append(i+1) if nums[i]> 0
        return res