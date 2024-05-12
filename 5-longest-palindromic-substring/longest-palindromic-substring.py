class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPalindrome(left, right):
            palindrom_len = 0 if left != right else -1
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
                palindrom_len += 2
            return s[left + 1:right]
        
        max_str = ""
        start_index = len(s)
        for i in range(len(s)):
            odd = checkPalindrome(i, i)
            even = checkPalindrome(i, i + 1)
            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
        return max_str
