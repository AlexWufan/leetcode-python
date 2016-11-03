class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float('inf')
        maxprofit = 0
        for x in prices:
        	if x < minprice:
        		minprice = x
        	elif x - minprice > maxprofit:
        		maxprofit = x -minprice
        	
        return maxprofit
if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.maxProfit([7, 1, 5, 3, 6, 4]))

#动态规划， kadane algorithm

def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit