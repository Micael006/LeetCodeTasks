class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def reverse_row(arr):
            for i in range(len(arr)):
                arr[i] = 1 - arr[i]
            return arr

        def reverse_col(matrix, col_num):
            for i in range(len(matrix)):
                matrix[i][col_num] = 1 - matrix[i][col_num]
            return matrix
        
        for i in range(len(grid)):
            if grid[i][0] == 0:
                grid[i] = reverse_row(grid[i])
        for j in range(1, len(grid[0])):
            cur_sum = 0
            for i in range(len(grid)):
                cur_sum += grid[i][j]
            if len(grid) - cur_sum > cur_sum:
                grid = reverse_col(grid, j)
        
        answer = 0
        for j in range(len(grid[0])):
            helper = 0
            for i in range(len(grid)):
                helper += grid[i][j]
            answer += helper * 2**(len(grid[0]) - 1 - j)
        return answer

