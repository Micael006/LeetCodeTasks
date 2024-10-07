class Solution:
    def minLength(self, s: str) -> int:
        stack = ['0']
        for elem in s:
            cur_pair = stack[-1] + elem
            if cur_pair == 'AB' or cur_pair == 'CD':
                stack.pop()
            else:
                stack.append(elem)
        return len(stack) - 1