class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        output = []
        d= {}
        pdic = {}
        if len(s) < len(p): return output
        window = s[0:len(p)]
        window = list(window)
        for x in window:
        	d[x] = d.get(x, 0) + 1
        for x in p:
        	pdic[x] = pdic.get(x, 0) + 1
        if d == pdic: output.append(0)

        for i in range(len(p),len(s)):
        	
        	d[window[0]] -= 1
        	if d[window[0]] == 0:
        		del d[window[0]]
        	del window[0]
        	window.append(s[i])
        	d[window[-1]] = d.get(window[-1], 0) + 1
        	
        	if d == pdic:
        		output.append(i-len(p)+1)
        return output

if __name__=='__main__':
    asolution = Solution()
    print(asolution.findAnagrams("cbaebabacd", "abc"))