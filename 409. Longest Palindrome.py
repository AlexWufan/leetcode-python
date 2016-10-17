class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = set()
        for x in s:
        	if x in a :
        		a.remove(x)
        	else :
        		a.add(x)
        return len(s)-len(a) if a else len(s)-len(a)+1