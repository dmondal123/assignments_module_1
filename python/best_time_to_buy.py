def maxProfit(self, prices) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            curProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(curProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit