class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(matrix)):
            cur_min = [max(matrix[i]), -1]
            for j in range(len(matrix[i])):
                if matrix[i][j] < cur_min[0]:
                    cur_min = [matrix[i][j], j]

            cur_max = [-1, -1]
            for j in range(len(matrix)):
                if matrix[j][cur_min[1]] > cur_max[0]:
                    cur_max = [matrix[j][cur_min[1]], j]

            if i == cur_max[1]:
                return [cur_min[0]]
        
        return []