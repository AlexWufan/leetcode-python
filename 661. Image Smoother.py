class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M[0])
        n = len(M)
        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                count = 0
                for x,y in [(-1,-1),(0,-1),(-1,0),(0,0),(1,0),(0,1),(1,1),(1,-1),(-1,1)]:
                    if 0 <= j + x <= m-1 and  0 <= i + y <= n-1:
                        res[i][j] += M[i+y][j+x]
                        count += 1
                res[i][j] = res[i][j]/count
        return res
        