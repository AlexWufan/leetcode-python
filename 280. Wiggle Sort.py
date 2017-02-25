class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if i%2 == 0 and i!= 0:
                if nums[i-1]<nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
            elif nums[i-1]>nums[i] and i!= 0:
                nums[i-1], nums[i] = nums[i], nums[i-1]