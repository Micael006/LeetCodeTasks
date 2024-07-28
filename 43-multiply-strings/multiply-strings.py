class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        answer = [0] * (len(num1) + len(num2))
        extra = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                cur = int(num1[i]) * int(num2[j])
                z = 0
                while cur > 0:
                    answer[i + j + z] += cur % 10
                    cur //= 10
                    z += 1

        extra = 0
        for i in range(len(answer)):
            answer[i] += extra
            extra = answer[i] // 10
            answer[i] %= 10

        while answer[-1] == 0:
            answer.pop()

        return ''.join([str(x) for x in answer[::-1]])            

