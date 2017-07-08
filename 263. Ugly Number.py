class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num > 1 :
            if num % 2 == 0:
                num //= 2
            elif num % 3 == 0:
                num //= 3
            elif num % 5 == 0:
                num //= 5
            else:
                break
        return num == 1