class Solution:
    def maximumSwap(self, num: int) -> int:
        answer = num
        str_num = str(num)
        for i in range(len(str_num) - 1):
            for j in range(i + 1, len(str_num)):
                answer = max(answer, int(str_num[:i] + str_num[j] + str_num[i+1:j] + str_num[i] + str_num[j+1:]))
        
        return answer