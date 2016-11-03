class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for n in nums:
        	if n == 0:
        		nums.remove(n)
        		nums.append(0)
        # return nums

if __name__ == '__main__':
	aSolution = Solution()
	print(aSolution.moveZeroes([0, 1, 0, 0, 3, 12,0]))



# in-place
def moveZeroes(self, nums):
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1


# inplace sort, 3.0中删掉了
nums.sort(cmp= lambda a, b: -1 if b == 0 else 0)