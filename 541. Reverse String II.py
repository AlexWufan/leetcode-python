class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        for i in range(0,len(s),k):
            if (i//k)%2 == 0:
                tmp = s[i:i+k]
                res+=tmp[::-1]
            elif (i//k)%2 == 1:
                res+=s[i:i+k]
        if len(s)-len(res)>0:
            if (i//k)%2 == 0:
                tmp = s[i:]
                res+=tmp[::-1]
            else:
                res+=s[i:]
        return res

# leetcode discuss
    def reverseStr(self, s, k):
        s = list(s)
        for i in xrange(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)