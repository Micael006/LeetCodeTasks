class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        emptyBottles = 0
        while numBottles > 0:
            ans += numBottles
            emptyBottles += numBottles % numExchange
            numBottles = numBottles // numExchange + emptyBottles // numExchange
            emptyBottles %= numExchange
        return ans