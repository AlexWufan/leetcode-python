class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums)) :
        	if nums[i] != i :
        		return i
        	elif i == len(nums)-1:
        		if nums[i] == i:
        			return i+1
        		else: return i
        


if __name__ == '__main__':
	aSolution  = Solution()
	print(aSolution.missingNumber([1,0]))

# 求和
def missingNumber(self, nums):
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)

# set
def missingNumber(self, nums):
    return (set(range(len(nums)+1)) - set(nums)).pop()