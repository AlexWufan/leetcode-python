class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for x in s:
        	res = res * 26 + ord(x)-64
        return res

if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.titleToNumber('AC'))

# 一行，reduce的第三个参数代表初始值
# return reduce(lambda x, y: 26*x+ord(y)-64, s, 0)