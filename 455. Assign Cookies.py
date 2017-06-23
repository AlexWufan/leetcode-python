class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        g.sort()
        s.sort()
        if s[-1]<g[0]:return 0

        p, q = 0, 0
        while p < len(g) and q < len(s):
            if g[p] <= s[q]:
                res += 1
                p+=1
                q+=1
            elif g[p] > s[q]:
                q+=1
        return res