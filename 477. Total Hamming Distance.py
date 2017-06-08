class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            bitcount = 0
            for num in nums:
                if num >> i & 1 == 1:
                    bitcount+=1
            res += bitcount*(len(nums)-bitcount)
        return res