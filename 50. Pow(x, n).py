class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n%2 == 0:
            return self.myPow(x*x,n/2)
        else:
            return x*self.myPow(x*x,n/2)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        while n:
            if n&1:
                res *= x
            x*=x
            n>>=1
        return res
            