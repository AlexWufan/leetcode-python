class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t = list(t)
        s = list(s)
        for i in range(len(s)):
            t.remove(s[i])
        return t[0]

# 更好的解法 dictionary
class Solution(object):
    """
    dictionary
    """
    def findTheDifference(self, s, t):
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        for ch in t:
            if dic.get(ch, 0) == 0:
                return ch
            else:
                dic[ch] -= 1



from collections import Counter


class Solution(object):
    def findTheDifference(self, s, t):
        return (Counter(t) - Counter(s)).popitem()[0]


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        k = 0
        for i in range(len(s)):
            k -= ord(s[i])
            k += ord(t[i])
            
        k+=ord(t[-1])
        return chr(k)