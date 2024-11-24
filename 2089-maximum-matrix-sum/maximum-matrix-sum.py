class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        cur_min = 10**10
        cur_sum = 0
        negative_count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                cur_min = min(cur_min, abs(matrix[i][j]))
                cur_sum += abs(matrix[i][j])
                negative_count += matrix[i][j] < 0
        
        if negative_count % 2:
            cur_sum -= 2 * cur_min
        
        return cur_sum