class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i and nums[i]==nums[i-1]:continue
            target = 0 - nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l]+nums[r] == target:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]: l += 1
                    while l<r and nums[r] == nums[r-1]: r -= 1
                    r-=1
                    l+=1
                elif nums[l]+nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return res