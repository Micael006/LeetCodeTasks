import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        stack = []
        start = 0
        i = int(expression[0] == '-')
        while i < len(expression):
            if expression[i] in '-+/':
                stack.append(int(expression[start:i]))
                start = i + (expression[i] == '/')
                i += 2
            else:
                i += 1
        
        stack.append(int(expression[start:len(expression)]))
        numerator = stack[0]
        denominator = stack[1]

        for j in range(2, len(stack), 2):
            numerator = numerator * stack[j + 1] + stack[j] * denominator
            denominator *= stack[j + 1]
            divider = math.gcd(abs(numerator), abs(denominator))
            numerator //= divider
            denominator //= divider
        
        return f'{numerator}/{denominator}'