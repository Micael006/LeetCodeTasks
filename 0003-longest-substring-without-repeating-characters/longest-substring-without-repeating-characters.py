class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        alphabet = dict()
        start, end = 0, 0
        max_len = 0
        for i in range(len(s)):
            if alphabet.get(s[i]) is not None:
                max_len = max(end - start + 1, max_len)
                start = max(alphabet[s[i]] + 1, start)
            alphabet[s[i]] = i
            end = i
        max_len = max(end - start + 1, max_len)
        return max_len