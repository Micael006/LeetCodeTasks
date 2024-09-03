class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join([str(ord(x) - ord('a') + 1) for x in s])
        for i in range(k):
            s = sum([int(x) for x in str(s)])
        
        return s