class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub_string = set()
        l = 0

        for i in range(len(s)):
            if s[i] not in sub_string:
                sub_string.add(s[i])
            else:
                max_len = max(max_len, len(sub_string))
                while s[i] in sub_string:
                    sub_string.discard(s[l])
                    l += 1
                sub_string.add(s[i])
        
        return max(max_len, len(sub_string))