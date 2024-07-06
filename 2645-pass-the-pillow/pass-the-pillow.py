class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rotation = time // (n - 1)
        if rotation % 2 == 0:
            return (time - rotation * (n - 1)) % n + 1
        else:
            return (n - 1) - ((time - rotation * (n - 1)) % n) + 1
        