class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:return m*n
        X, Y = zip(*ops)
        # min_i = float('inf')
        # min_j = float('inf')
        # for op in ops:
        #     min_i = min(min_i, op[0])
        #     min_j = min(min_j, op[1])
        return min(X)*min(Y)