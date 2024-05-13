class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            cur_min = min(cur_min, prices[i])
            if prices[i] > prices[i - 1]:
                max_profit = max(max_profit, prices[i] - cur_min)
        return max_profit