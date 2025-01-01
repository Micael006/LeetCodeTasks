class Solution:
    def maxScore(self, s: str) -> int:
        answer = 0
        zeros_count = 0
        ones_count = s.count('1')
        answer = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_count += 1
            else:
                ones_count -= 1
            if zeros_count + ones_count > answer:
                answer = zeros_count + ones_count
        
        return answer