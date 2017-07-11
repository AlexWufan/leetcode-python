class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        p, q = 1, num

        while p<=q:
            mid = p+(q-p)//2
            if mid*mid > num:
                q = mid - 1
            elif mid*mid < num:
                p = mid + 1
            else:
                return True
        return False