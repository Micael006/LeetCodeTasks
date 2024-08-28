class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in range(len(s)):
            if s[i] not in check:
                stack.append(s[i])
            elif len(stack) > 0 and stack[-1] == check[s[i]]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
