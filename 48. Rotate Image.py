class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list, zip(*A[::-1]))

        # matrix[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]
        # A.reverse()
        # for i in range(len(A)):
        #     for j in range(i):
        #         A[i][j], A[j][i] = A[j][i], A[i][j]