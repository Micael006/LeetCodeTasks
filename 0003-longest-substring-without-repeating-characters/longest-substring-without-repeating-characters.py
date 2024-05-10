class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alphabet = dict()
        max_len = 0
        cur_len = 0
        left = 0
        for i in range(len(s)):
            if alphabet.get(s[i]) is None:
                alphabet[s[i]] = i
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                left = max(left, alphabet[s[i]] + 1)
                cur_len = i - left + 1
                alphabet[s[i]] = i
        max_len = max(max_len, cur_len)
        return max_len