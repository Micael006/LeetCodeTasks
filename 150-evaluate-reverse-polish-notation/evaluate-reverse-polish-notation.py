class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].isdigit() or tokens[i][1:].isdigit():
                stack.append(int(tokens[i]))
            else:
                x, y = stack[-2], stack[-1]
                stack.pop()
                stack.pop()
                if tokens[i] == '+':
                    stack.append(x + y)
                elif tokens[i] == '-':
                    stack.append(x - y)
                elif tokens[i] == '*':
                    stack.append(x * y)
                else:
                    stack.append(int(x / y))

        return stack[0]