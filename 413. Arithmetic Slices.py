class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        dp = [0 for _ in A]
        for i in range(2,len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 0
        return sum(dp)

if __name__ == '__main__':
    Asolution = Solution()
    print(Asolution.numberOfArithmeticSlices([1,2,3,4,5]))