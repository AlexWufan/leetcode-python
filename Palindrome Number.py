class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 : return False
        elif x == 0 : return True
        else:
        	y = 0
        	temp = x
        	while x:
        		y = y*10 + x %10
        		x //= 10
        		if y == temp : return True
        	return False

        # return str(x)==str(x)[::-1]

if __name__=='__main__':
    asolution = Solution()
    print(asolution.isPalindrome(1234321))
