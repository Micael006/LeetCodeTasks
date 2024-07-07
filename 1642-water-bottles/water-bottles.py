class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        emptyBottles = 0
        while numBottles > 0:
            ans += numBottles
            emptyBottles += numBottles % numExchange
            numBottles //= numExchange
            numBottles += emptyBottles // numExchange
            emptyBottles %= numExchange
        return ans