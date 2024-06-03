class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pos = 0
        for i in range(len(s)):
            if s[i] == t[pos]:
                pos += 1
                if pos == len(t):
                    break
        return len(t) - pos