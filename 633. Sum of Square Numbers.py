class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(c**0.5)+1):
            b = (c-a*a)**0.5
            if b == int(b):
                return True
        return False