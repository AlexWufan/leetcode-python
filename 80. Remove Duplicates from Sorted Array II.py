class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1: return len(nums)
        flag = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[flag] == nums[i] and count == 2:
                continue
            elif nums[flag] == nums[i] and count < 2:
                nums[flag+1] = nums[i]
                count += 1
                flag += 1
            else:
                count = 1
                nums[flag+1] = nums[i]
                flag += 1

        return flag+1

if __name__=='__main__':
    asolution = Solution()
    print(asolution.removeDuplicates([1,1,1,1,2,2,3,3,3,3,3,3,4,4,5,6,6]))



# better one
# def removeDuplicates(self, nums):
#     i = 0
#     for n in nums:
#         if i < 2 or n > nums[i-2]:
#             nums[i] = n
#             i += 1
#     return i