class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1: return len(nums)
        flag = 0
        for i in range(1, len(nums)):
        	if nums[flag] == nums[i]:
        		continue
        	else: 
        		nums[flag+1] = nums[i]
        		flag += 1

        return flag+1

if __name__=='__main__':
    asolution = Solution()
    print(asolution.removeDuplicates([1,1,1,1,2,2,3,3,3,3,3,3,4,4,5,6,6]))
