class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        res = 0
        dp = [[1 for _ in range(n)] for _ in range(n)]

        for length in range(2,n):
        	for i in range(n-length+1):
        		j = i + length-1
        		if s[i]==s[j]:
        			dp[i][j] = dp[i+1][j-1] + 2
        		else:
        			dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return max(dp)