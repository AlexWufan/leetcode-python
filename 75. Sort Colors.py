class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start, end  = 0, len(nums)-1
        i = 0
        while i in range(len(nums)):
        	if nums[i] == 2 and i < end:
        		nums[i], nums[end] = nums[end], nums[i]
        		end -= 1
        	elif nums[i] == 0 and i > start:
        		nums[i], nums[start] = nums[start], nums[i]
        		start += 1
        	else:
        		i += 1
        print(nums)

        # 另外一种解法
    def sortColors(self, nums):
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
            print(nums)
            
if __name__=='__main__':
    asolution = Solution()
    print(asolution.sortColors([1,0,2,1,2,0,1,0,1]))