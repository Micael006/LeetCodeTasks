class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        def checkPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    break
                left += 1
                right -= 1
            
            return left, right, left >= right

        l, r, _ = checkPalindrome(s, 0, len(s) - 1)

        _, _, ans = checkPalindrome(s, l + 1, r)
        _, _, t_ans = checkPalindrome(s, l, r - 1)
        return ans or t_ans
