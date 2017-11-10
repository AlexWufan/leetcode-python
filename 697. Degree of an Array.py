class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        left, right, count = {}, {}, {}
        for index,value in enumerate(nums):
            if value not in left:
                left[value] = index
            right[value] = index
            count[value] = count.get(value,0) + 1
        
        degree = max(count.values())
        
        for key in count:
            if count[key] == degree:
                res = min(right[key]-left[key] +1, res)
        return res
            