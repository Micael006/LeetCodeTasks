class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        answer = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    answer += 1
                    z = 1
                    while i + z < len(matrix) and j + z < len(matrix[i]):
                        another_one = True
                        for k in range(z):
                            if matrix[i + k][j + z] == 0 or matrix[i + z][j + k] == 0:
                                another_one = False
                                break
                        
                        if matrix[i + z][j + z] == 0:
                            another_one = False
                        
                        if not another_one:
                            break
                        
                        answer += 1
                        z += 1

        return answer