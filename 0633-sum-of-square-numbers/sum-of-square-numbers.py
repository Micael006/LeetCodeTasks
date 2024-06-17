class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c**0.5 == int(c**0.5):
            return True
        for i in range(1, int(c**0.5) + 1):
            cur = (c - i**2)**0.5
            if cur == int(cur):
                return True
        return False    