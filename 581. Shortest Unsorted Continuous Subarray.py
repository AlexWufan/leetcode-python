class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(nums)
        start, end = len(nums)-1, 0
        for i in range(len(nums)):
            if a[i] != nums[i]:
                start =  min(i, start)
                end = max(i, end)
        if end - start > 0:
            return end - start + 1
        else:
            return 0
                