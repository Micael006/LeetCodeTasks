class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        answer = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[i]) - 2):
                rows = [sum(grid[i][j:j+3]), sum(grid[i + 1][j:j+3]), sum(grid[i + 2][j:j+3])]
                cols = [
                    grid[i][j] + grid[i + 1][j] + grid[i + 2][j],
                    grid[i][j+1] + grid[i + 1][j+1] + grid[i + 2][j+1],
                    grid[i][j+2] + grid[i + 1][j+2] + grid[i + 2][j+2],
                ]
                diags = [
                    grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2],
                    grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
                ]
                if len(set(rows + cols + diags)) == 1 and sorted(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]) == list(range(1, 10)):
                    answer += 1
        
        return answer
