class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i in range(len(nums)):
        	if nums[i] in d and i-d.get(nums[i]<=k):
        		return True
        	d[nums[i]] = i
        return False

#better
		d = {}
        for i, n in enumerate(nums):
        	if n in d and i - d[n]<=k:
        		return True
        	d[n] = i
        return False