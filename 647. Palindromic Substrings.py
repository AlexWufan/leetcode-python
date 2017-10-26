class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        counter = 0
        for i in range(len(s)):
            counter = self.extend(s,i,i,counter)
            counter = self.extend(s,i,i+1,counter)
        return counter
    
    def extend(self, s, left, right, counter):
        while left>=0 and right<len(s) and s[left] == s[right]:
            counter += 1
            left -= 1
            right +=1
        return counter

