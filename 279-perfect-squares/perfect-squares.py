import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            cur_min = 2**32
            while j * j <= i:
                remains = i - j * j
                cur_min = min(cur_min, dp[remains])
                j += 1
            dp[i] = cur_min + 1
        return dp[-1]