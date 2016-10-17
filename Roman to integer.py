class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = dic[s[0]]
        for i in range(1,len(s)):
        	if dic[s[i-1]] >= dic[s[i]]:
        		sum = sum + dic[s[i]]
        	else:
        		sum = sum - 2*dic[s[i-1]] + dic[s[i]]
        return sum

if __name__=='__main__':
    asolution = Solution()
    print(asolution.romanToInt('MCDXXXVII'))