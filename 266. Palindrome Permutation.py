class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = set()
        for x in s:
            if x in a:
                a.remove(x)
            else:
                a.add(x)
        return len(a) == 1 or len(a) == 0

# 一行
    def canPermutePalindrome(self, s):
        return sum(v % 2 for v in collections.Counter(s).values()) < 2