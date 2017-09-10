class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l<r:
            mid = l+(r-l)//2
            if nums[mid-1]==nums[mid]:
                if mid%2 == 0:
                    r = mid-2
                else:
                    l = mid+1
            elif nums[mid] == nums[mid+1]:
                if mid%2 == 0:
                    l = mid+2
                else:
                    r = mid-1
            else:
                return nums[mid]
        return nums[l]

# 更好的做法，
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l<r:
            mid = l+(r-l)//2
            if mid%2 == 1:
                mid -= 1
            if nums[mid] != nums[mid+1]:
                r = mid
            else:
                l = mid + 2
        return nums[l]
                