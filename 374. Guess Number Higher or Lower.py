# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n
        while 1:
            mid = (l + h) // 2
            if guess(mid) == 1:
                l = mid + 1
            elif guess(mid) == -1:
                h = mid
            else:
                return mid