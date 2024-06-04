class Solution:
    def longestPalindrome(self, s: str) -> int:
        found = set()
        count = 0
        for i in range(len(s)):
            if s[i] in found:
                count += 2
                found.discard(s[i])
            else:
                found.add(s[i])
        if len(found) > 0:
            count += 1
        return count