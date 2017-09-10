class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(n,'', n, n,res)
        return res
    
    def dfs(self, n, path, left, right, res):
        if len(path) == 2*n:
            res.append(path)
            return None
        if left:
            self.dfs(n, path+'(', left-1, right, res)
        if left<right:
            self.dfs(n, path+')', left, right-1, res)

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(n,'', res)
        return res
    
    def dfs(self, n, path, res):
        if len(path) == 2*n:
            res.append(path)
            return None
        if path.count('(') < n and path.count(')') == path.count('('):
            self.dfs(n, path + '(', res)
        elif path.count('(') < n and path.count(')') < path.count('('):
            self.dfs(n, path + '(', res)
            self.dfs(n, path + ')', res)
        elif path.count('(') == n and path.count(')') < n:
            self.dfs(n, path + ')', res)

if __name__=='__main__':
    asolution = Solution()
    print(asolution.generateParenthesis(3))