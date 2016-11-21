class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    res+=4
                    if j-1>=0 and grid[i][j-1]:
                        res-=1
                    if j+1<n and grid[i][j+1]:
                        res-=1
                    if i-1>=0 and grid[i-1][j]:
                        res-=1
                    if i+1<n and grid[i+1][j]:
                        res-=1
        return res