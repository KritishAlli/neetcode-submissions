class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        for i in range(len(prices)):
            minBuy = min(minBuy, prices[i])

            maxP = max(maxP, prices[i]-minBuy)

        return maxP
        