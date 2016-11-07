class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = min(nums)
        return sum(nums[i]-minimum for i in range(len(nums)))
        # or
        return sum(nums)-len(nums)*min(nums)

if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.minMoves([1,2,4]))