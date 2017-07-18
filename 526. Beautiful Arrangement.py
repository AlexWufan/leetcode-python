class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(i,X,cache = {}):
            if i == 1:
                return 1
            if X not in cache:
                cache[X] = sum(helper(i-1,X[:j]+X[j+1:])
                           for j,x in enumerate(X)
                           if x % i == 0 or i % x == 0)
            return cache[X]
        return helper(N, tuple(range(1,N+1)))

#上面的是top down, 并且存了cache,90ms.
#下面的是backtracking, 2300ms



class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = [0]
        array = []
        used = [False for _ in range(N)]
        self.dfs( array, res, used, N)
        return res[0]
    
    def dfs(self, array, res, used, num):
        if len(array) == num:
            res[0] += 1
            return
        for i in range(1,num+1):
            if not used[i-1] and (i % (len(array)+1) == 0 or (len(array)+1) % i == 0):
                used[i-1] = True
                self.dfs(array+[i], res, used, num)
                used[i-1] = False 
                