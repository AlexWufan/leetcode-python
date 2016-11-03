class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-k:]+(nums[:-k])

if __name__ == '__main__':
	aSolution  = Solution()
	print(aSolution.rotate([1,2,3,4,5,6,7],3))