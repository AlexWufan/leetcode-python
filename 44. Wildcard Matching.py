class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        if len(p) - p.count('*') > len(s):
            return False
        dp = [True] + [False] * len(s)
        for i in p:
            if i != '*':
                for n in range(len(s)-1,-1,-1):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, len(s)+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]
        
class Solution:
# @return a boolean
def isMatch(self, s, p):
    length = len(s)
    if len(p) - p.count('*') > length:
        return False
    dp = [True] + [False]*length
    for i in p:
        if i != '*':
            for n in reversed(range(length)):
                dp[n+1] = dp[n] and (i == s[n] or i == '?')
        else:
            for n in range(1, length+1):
                dp[n] = dp[n-1] or dp[n]
        dp[0] = dp[0] and i == '*'
    return dp[-1]