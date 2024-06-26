class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        d = dict()
        l = 0

        for i in range(len(s)):
            if not (s[i] not in d or d[s[i]] < l):
                max_len = max(i - l, max_len)
                l = d[s[i]] + 1
            d[s[i]] = i
        
        return max(max_len, len(s) - l)