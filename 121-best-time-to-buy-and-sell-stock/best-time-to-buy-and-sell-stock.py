class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_min = prices[0]

        for i in range(1, len(prices)):
            cur_min = min(cur_min, prices[i])
            max_profit = max(prices[i] - cur_min, max_profit)
        
        return max_profit