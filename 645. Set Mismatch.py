class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup, mis = None, None
        res = [0 for _ in nums]
        for num in nums:
            res[num-1] += 1
        for i in range(1,len(nums)+1):
            if res[i-1] == 2:
                dup = i
            elif res[i-1] == 0:
                mis = i
        return [dup, mis]