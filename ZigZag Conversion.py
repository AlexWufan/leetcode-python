class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # slist = list[s]
        zigzag = ['' for i in range(numRows)]
        i = 0
        step = 1
        if numRows ==1:
        	return s
        for ltr in s:
        	zigzag[i] += ltr
        	if i == numRows-1:
        		step = -1
        	if i == 0:
        		step = 1
        	i = i + step
        return ''.join(zigzag)

if __name__=='__main__':
    asolution = Solution()
    print(asolution.convert("PAYPALISHIRING", 100))