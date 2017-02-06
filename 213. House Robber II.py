class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        return max(self.robber(nums[1:]), self.robber(nums[:-1]))
        
    def robber(self,nums):
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last+i, now)
        return now

#stefen's solution.
class Solution:
    def rob(self, nums):
        def rob(nums):
            now = prev = 0
            for n in nums:
                now, prev = max(now, prev + n), now
            return now
        return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))