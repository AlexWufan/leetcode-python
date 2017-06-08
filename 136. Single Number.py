class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for x in nums:
        	if x in s:
        		s.remove(x)
        	else:
        		s.add(s)
        return list(s)

# better

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums)))*2 - sum(nums)

def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return sum(list(set(nums)))*2 - sum(nums)
        # bit manipulation
        res = 0
        for num in nums:
            res ^= num
        return res