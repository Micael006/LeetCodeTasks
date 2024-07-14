class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq_count = dict()
        max_str_len = 0

        for r in range(len(s)):
            if not s[r] in freq_count:
                freq_count[s[r]] = 0
            freq_count[s[r]] += 1

            cur_str_len = r - l + 1
            if cur_str_len - max(freq_count.values()) <= k:
                max_str_len = max(max_str_len, cur_str_len)
            else:
                freq_count[s[l]] -= 1
                if freq_count[s[l]] == 0:
                    del freq_count[s[l]]
                l += 1
        
        return max_str_len