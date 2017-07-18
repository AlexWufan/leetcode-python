class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(i,X):
            if i == 1:
                return 1
            return sum(helper(i-1,X-{x})
                        for x in X
                       if x % i == 0 or i % x == 0)
        return helper(N, set(range(1,N+1)))


#上面的是top down, 200ms，还可以提升性能.
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
                