class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0,0]
        xor = 0
        for num in nums:
            xor ^= num
        xor &= -xor
        for num in nums:
            if xor&num == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res