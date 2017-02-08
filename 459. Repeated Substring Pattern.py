class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        longstr = (str+str)[1:-1]
        
        return longstr.find(str) != -1

        # better one
        # return str in (str+str)[1:-1]