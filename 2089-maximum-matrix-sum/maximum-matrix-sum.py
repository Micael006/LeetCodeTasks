class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        cur_min = 10**10
        cur_sum = 0
        negative_count = 0
        abs_elem = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                abs_elem = abs(matrix[i][j])
                if abs_elem < cur_min:
                    cur_min = abs_elem
                cur_sum += abs_elem
                if matrix[i][j] < 0:
                    negative_count += 1
        
        if negative_count % 2:
            cur_sum -= 2 * cur_min
        
        return cur_sum