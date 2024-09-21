class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        answer = []
        cur = 1
        while len(answer) < n:
            while cur <= n:
                answer.append(cur)
                cur *= 10
            cur //= 10
            for i in range(1, 10 - cur % 10):
                if cur + i <= n:
                    answer.append(cur + i)
                    if cur + i == 99:
                        print(len(answer))
            cur //= 10
            cur += 1
            while cur % 10 == 0:
                cur //= 10

        return answer