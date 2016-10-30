class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = [1] * len(nums)
        temp = 1
        for i in range(len(nums)):
        	output[i] = temp
        	temp = temp * nums[i]
        temp = 1
        for i in range(len(nums)-1,-1,-1):
        	output[i] *= temp
        	temp = temp * nums[i]
        return output


if __name__ == '__main__':
	aSolution  = Solution()
	print(aSolution.productExceptSelf([1,2,3,4]))


# 两步到位，时间复杂度是o(n)!如果用两层循环就是o(n)太慢了