class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        start, end = 0, 0
        res = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                end = i
            else:
                start = i
                end = i
            res = max(res, end - start + 1)
        return res