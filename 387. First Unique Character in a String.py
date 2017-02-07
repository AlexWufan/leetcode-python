class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = 'abcdefghijklmnopqistuvwxyz'
        index = [s.index(x) for x in alphabet if s.count(x)==1]
        return min(index) if index else -1