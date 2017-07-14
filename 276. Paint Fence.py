class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if not n or not k:
            return 0
        elif n == 1:
            return k
        diff = k*(k-1)
        same = k
        for i in range(2,n):
            diff, same = (diff+same) * (k-1), diff
            
        return diff + same