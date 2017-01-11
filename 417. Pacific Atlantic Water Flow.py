class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        res = []
        m = len(matrix)
        n = len(matrix[0])
        p = [[False for cell in range(n)] for cell in range(m)]
        a = [[False for cell in range(n)] for cell in range(m)]
        for i in range(m):
        	self.dfs(matrix, i, 0, p, m, n)
        	self.dfs(matrix, i, n-1, a, m, n)
        for j in range(n):
        	self.dfs(matrix, 0, j, p, m, n)
        	self.dfs(matrix, m-1, j, a, m, n)
        for i in range(m):
        	for j in range(n):
        		if a[i][j] == p[i][j] == True:
        			res.append([i,j])
        return res

    def dfs(self,matrix, i, j, visited, m, n):
    	visited[i][j] = True
    	for cordinate in [(1,0),(-1,0),(0,1),(0,-1)]:
    		x, y = i + cordinate[0], j + cordinate[1]
    		if 0<=x<m and 0<=y<n and visited[x][y] == False and matrix[i][j] <= matrix[x][y]:
    			self.dfs(matrix, x, y, visited, m, n)