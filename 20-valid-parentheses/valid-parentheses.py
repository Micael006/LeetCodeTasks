class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in '([{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                l = ')]}'.find(s[i])
                r = '([{'.find(stack[-1])
                if l == r:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True