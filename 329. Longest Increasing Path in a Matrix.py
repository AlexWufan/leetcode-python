class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        cache = [[0 for cell in range(n)] for cell in range(m)]
        for i in range(m):
        	for j in range(n):
        		self.dfs(matrix, i, j, cache, m, n)
        return max(cache[i][j] for i in range(m) for j in range(n))

    def dfs(self, matrix, i, j, cache, m, n):
    	if cache[i][j]:
    		return cache[i][j]
    	recordmaxlength = 1
    	length = 1
    	for cordinate in [(1,0),(-1,0), (0,1),(0,-1)]:
    		x, y = i + cordinate[0], j + cordinate[1]
    		if 0<=x<m and 0<=y<n and matrix[i][j] < matrix[x][y]:
    			length = 1 + self.dfs(matrix, x, y, cache, m, n)
    			print(recordmaxlength, length)
    			recordmaxlength = max(recordmaxlength, length)
    		else: continue
    	cache[i][j] = recordmaxlength
    	return cache[i][j]

if __name__=='__main__':
    asolution = Solution()
    print(asolution.longestIncreasingPath([[7,7,5],[2,4,6],[8,2,0]]))


#更好的做法，
	# def longestIncreasingPath(self, matrix):
	#     def dfs(i, j):
	#         if not dp[i][j]:
	#             val = matrix[i][j]
	#             dp[i][j] = 1 + max(
	#                 dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
	#                 dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
	#                 dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
	#                 dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
	#         return dp[i][j]

	#     if not matrix or not matrix[0]: return 0
	#     M, N = len(matrix), len(matrix[0])
	#     dp = [[0] * N for i in range(M)]
	#     return max(dfs(x, y) for x in range(M) for y in range(N))