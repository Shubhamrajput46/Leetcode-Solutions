class Solution(object):
    def maxProfit(self, prices):
        minPrice=prices[0]
        profit = 0

        for i in range(1, len(prices)):
            currProfit=prices[i] - minPrice
            if currProfit > profit:
                profit = currProfit
            minPrice = min(minPrice,prices[i])
        
        return profit
        
        