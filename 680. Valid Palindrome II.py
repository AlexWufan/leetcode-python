class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left]!=s[right]:
                return self.check(s[left:right]) or self.check(s[left+1:right + 1])
            else:
                left += 1
                right -= 1
        return True
    
    def check(self,s):
        return s == s[::-1]