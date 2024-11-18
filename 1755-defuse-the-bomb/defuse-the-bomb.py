class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        
        code_len = len(code)
        code *= 3
        answer = []
        if k > 0:
            for i in range(code_len):
                answer.append(sum(code[i + code_len + 1:i + code_len + k + 1]))
        else:
            for i in range(code_len):
                answer.append(sum(code[i + code_len + k : i + code_len]))
        
        return answer