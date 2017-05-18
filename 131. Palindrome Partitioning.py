class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs( res, s, [])
        return res
        
    def dfs(self, res, s, path):
        if not s:
            res.append(path)
        for i in range(1,len(s)+1):
            if self.isPar(s[:i]):
                self.dfs(res, s[i:], path+[s[:i]])
                
    def isPar(self,s):
        return s == s[::-1]