class Solution:
    def minimumSteps(self, s: str) -> int:
        extra = 0
        answer = 0
        for i in range(len(s) - 1, -1 ,-1):
            if s[i] == '1':
                answer += (len(s) - 1) - i - extra
                extra += 1

        return answer