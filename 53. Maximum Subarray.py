class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        maxNum = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i],dp[i-1]+nums[i])
            maxNum = max(dp[i], maxNum)
        return maxNum