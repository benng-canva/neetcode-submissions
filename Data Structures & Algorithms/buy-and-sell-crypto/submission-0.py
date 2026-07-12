class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, maxProfit = 0, 0, 0

        while sell < len(prices):
            curProfit = prices[sell] - prices[buy]
            maxProfit = max(maxProfit, curProfit)

            if prices[sell] < prices[buy]:
                buy = sell

            sell += 1

        return maxProfit
        