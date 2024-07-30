class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        for i in range(len(mat)):
            answer += mat[i][i]

            if len(mat) - i - 1 != i:
                answer += mat[i][len(mat) - i - 1]

        return answer