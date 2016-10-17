class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = ''
        if strs == []:
        	return lcp
        for i in range(len(strs[0])):
            x = strs[0][i]
            for y in strs:
                if len(y)-i >= 1 and x == y[i]: pass
                else: return lcp
            lcp += x
        return lcp

if __name__=='__main__':
    asolution = Solution()
    print(asolution.longestCommonPrefix(['aa','a']))