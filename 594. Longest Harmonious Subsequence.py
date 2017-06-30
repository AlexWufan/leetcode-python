class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        res = 0
        for num in nums:
            count[num] = count.get(num,0) + 1
        for num in count:
            if num+1 in count:
                res = max(res, count[num]+count[num+1])
        return res