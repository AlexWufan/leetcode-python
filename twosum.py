class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brute force, bad
        # for i in range(len(nums)):
        #     x = nums[i]
        #     for j in range(len(nums)):
        #         y = nums[j]
        #         if x+y == target and i!=j :
        #             b = [i, j]
        #             return b

        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]]=i

if __name__=='__main__':
    asolution = Solution()
    print(asolution.twoSum([2, 7, 11, 15], 17))