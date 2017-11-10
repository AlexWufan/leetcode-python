class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, pre, cur = 0, 0, 1
        for i in range(1,len(s)):
            if s[i-1] != s[i]:
                res += min(pre, cur)
                pre = cur
                cur = 1
            else:
                cur += 1
        return res + min(pre, cur)