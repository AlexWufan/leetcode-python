class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window = sum(nums[:k])
        res = window
        for i in range(k,len(nums)):
            window = window + nums[i] - nums[i-k]
            res = max(res,window)
        return float(res)/k
        