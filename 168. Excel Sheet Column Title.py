class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
        	res = chr((n-1)%26+65) + res
        	n = (n-1)//26
        return res


        
if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.convertToTitle(284))