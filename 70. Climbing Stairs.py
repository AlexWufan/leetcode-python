class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [0 for x in range(n)]
        dp[0] = 1
        dp[1] = 2
        for x in range(2,n):
            dp[x] = dp[x-1]+dp[x-2]
        return dp[n-1]