class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
        	if prices[i]<prices[i+1]:
        		profit += prices[i+1]-prices[i]
        return profit
        # or one line
        # return sum(max(pirce[i+1]-prices[i], 0) for i in range(len(prices)-1))
        # return sum(b-a for a,b in zip(prices,prices[1:])if b>a)



if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.maxProfit([7, 1, 5, 3, 6, 4]))   