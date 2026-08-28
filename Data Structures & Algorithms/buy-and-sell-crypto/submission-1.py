class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0
        minbuy = prices[0]
        for i in range(0, len(prices)):
            if prices[i] - minbuy > maxprofit:
                maxprofit = prices[i] - minbuy
            if prices[i] < minbuy:
                minbuy = prices[i]
        return maxprofit
        
