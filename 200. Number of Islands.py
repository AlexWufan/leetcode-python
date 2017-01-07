class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
        	for j in range(len(grid[i])):
        		if grid[i][j] == '1':
        			res += 1
        			self.dfs(i,j, grid)
        return res

    def dfs(self, i, j, grid):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            self.dfs(i+1, j, grid)
            self.dfs(i-1, j, grid)
            self.dfs(i, j-1, grid)
            self.dfs(i, j+1, grid)
