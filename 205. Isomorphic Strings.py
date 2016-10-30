class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s,t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.isIsomorphic('paper','title'))