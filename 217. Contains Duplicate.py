class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = {}
        for x in nums:
            a[x] = a.get(x,0)+1
        for x in a:
            if a[x]>=2:
                return True
        return False
# 

len(nums) > len(set(nums))