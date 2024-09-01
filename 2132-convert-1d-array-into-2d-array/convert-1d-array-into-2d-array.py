class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        answer = []
        if m * n != len(original):
            return answer
        for i in range(m):
            answer.append(original[i*n:(i + 1)*n])
        return answer