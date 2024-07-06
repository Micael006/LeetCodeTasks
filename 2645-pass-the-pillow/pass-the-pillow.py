class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rotation = time // (n - 1)
        if rotation % 2 == 0:
            return time % (n - 1) + 1
        else:
            return n - time % (n - 1)
        