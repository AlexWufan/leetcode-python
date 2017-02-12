class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
        	dp[i][i] = True
        	if i-1>=0:
        		dp[i][i-1] = True
        maxlen = 0 if not s else 1
        res = s[0] if s else ''
        for length in range(2,n+1):
        	for i in range(n-length+1):
        		j = i+length-1
        		if dp[i+1][j-1] == True and s[i]==s[j]:
        			dp[i][j] = True
        			if length > maxlen:
        				maxlen = length
        				res = s[i:j+1]
        return res