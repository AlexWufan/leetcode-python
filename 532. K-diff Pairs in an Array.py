class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        if k == 0:
            for key,value in dict.items():
                if value >= 2:
                    res+=1
        elif k > 0:
            for key in dict:
                if key+k in dict:
                    res+=1
        else: res = 0
        return res