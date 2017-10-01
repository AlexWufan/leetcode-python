class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp  = [[0 for _ in matrix[0]] for _ in matrix]
        length = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if not i or not j: #防止边界情况
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j]:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                length = max(length, dp[i][j]);
        
        return length*length