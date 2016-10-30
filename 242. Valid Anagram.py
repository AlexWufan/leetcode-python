class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s)==sorted(t)
 # better
 # class Solution(object):
 #    def isAnagram(self, s, t):
 #        a, b ={}, {}
        # for x in s :
        #     a[x] = a.get(x,0)+1
        # for x in t :
        #     b[x] = b.get(x,0)+1
        # return a == b