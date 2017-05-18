# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        res = 1
        while start < end:
            res = start+(end-start)//2
            if isBadVersion(res):
                end = res
            else:
                start = res+1
        return start