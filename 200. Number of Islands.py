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

# 使用visited数组的办法。

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        res = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    res += 1
                    self.dfs(i,j,grid,visited)
        return res        
        
    def dfs(self,i,j,grid,visited):
        if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
            self.dfs(i+1,j, grid, visited)
            self.dfs(i,j+1, grid, visited)
            self.dfs(i-1,j, grid, visited)
            self.dfs(i,j-1, grid, visited)




