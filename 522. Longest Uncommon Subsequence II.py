class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def is_sub(s1,s2):
            s2 = iter(s2)
            return all(s in s2 for s in s1)
        strs = sorted(strs, key = len, reverse = True)
        for s in strs:
            if sum(is_sub(s,t) for t in strs) == 1:
                return len(s)
        return -1