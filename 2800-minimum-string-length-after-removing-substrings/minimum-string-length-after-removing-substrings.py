class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for elem in s:
            if stack and ((stack[-1] == 'A' and elem == 'B') or (stack[-1] == 'C' and elem == 'D')):
                stack.pop()
            else:
                stack.append(elem)
        return len(stack)