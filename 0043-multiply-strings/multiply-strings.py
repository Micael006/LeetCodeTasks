class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        answer = [0] * (len(num1) + len(num2))

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                answer[i + j] += int(num1[i]) * int(num2[j])
        
        overflow = 0
        for i in range(len(answer)):
            answer[i] += overflow
            overflow = answer[i] // 10
            answer[i] = str(answer[i] % 10)
        
        last_zero = len(answer)
        while answer[last_zero - 1] == '0':
            last_zero -= 1
        
        answer = answer[:last_zero]
        
        return ''.join(answer[::-1])

