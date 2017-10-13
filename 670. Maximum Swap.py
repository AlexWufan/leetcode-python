class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = [int(x) for x in str(num)]
        dp = [-1 for _ in range(len(num))]
        index = -1
        for i in range(len(num)-1,-1,-1):
            if i == (len(num) -1) or num[i]>dp[i+1][0]:
                dp[i] = (num[i],i)
            else:
                dp[i] = dp[i+1]
        for i in range(len(num)):
            if num[i] < dp[i][0]:
                index = i
                break
        num[i], num[dp[i][1]] = num[dp[i][1]], num[i]
        return  int(''.join(map(str,num)))
        