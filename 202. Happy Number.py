class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        h = []
        while n != 1:
        	if n in h:
        		return False
        	else:
        		h.append(n)
        	n = sum(int(x)**2 for x in str(n))
        return True

if __name__ == '__main__':
	aSolution = Solution()
	print(aSolution.isHappy(19))