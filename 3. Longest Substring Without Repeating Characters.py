class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        window = []
        for i in s:
        	print(window)
        	if i in window:
        		while 1:
        			del window[0]
        			if i not in window:
        				break
        	window.append(i)
        	if len(window)>m:
        		m = len(window)
        	else:
        		continue
        return m

if __name__=='__main__':
    asolution = Solution()
    print(asolution.lengthOfLongestSubstring('abcadbcbb'))

# better!
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

# 自己写下dict写法
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = {}
        start = 0
        res = 0
        for i in range(len(s)):
            if s[i] in window and start <= window[s[i]]:
                start = window[s[i]] + 1
            else:
                res = max(i - start + 1, res)
            window[s[i]] = i
            
        return res




