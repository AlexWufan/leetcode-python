class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num = self.dfs(i,j,grid)
                    print(num)
                    res = max(num, res)
        return res
        
    def dfs(self, i, j, grid):
        if 0<= i < len(grid) and 0<= j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + self.dfs(i+1,j,grid) + self.dfs(i-1,j,grid) + self.dfs(i,j+1,grid) + self.dfs(i,j-1,grid)
        else:
            return 0