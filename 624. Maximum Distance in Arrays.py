class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        res, MAX, MIN = 0, arrays[0][-1], arrays[0][0]
        for i in range(1, len(arrays)):
            res = max(res, abs(MAX - arrays[i][0]), abs(arrays[i][-1] - MIN ))
            MAX = max(MAX, arrays[i][-1])
            MIN = min(MIN, arrays[i][0])
        return res