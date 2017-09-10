class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l<r:
            mid = l+(r-l)/2
            if nums[r] < nums[mid]:
                l = mid+1
            else:
                r = mid
        return nums[l]

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l<r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = l+(r-l)/2
            if nums[l] <= nums[mid]:
                l = mid+1
            else:
                r = mid
        return nums[l]