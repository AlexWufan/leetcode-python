class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res,k,n,[],1)
        return res
        
    def dfs(self, res, k, n, path, index):
        if n < 0: return # pruning
        elif n == 0 and k == len(path):
            res.append(path)
        else:
            for i in range(index,10):
                if i > n: #pruning
                    break
                self.dfs(res, k, n-i, path+[i],i+1)
                