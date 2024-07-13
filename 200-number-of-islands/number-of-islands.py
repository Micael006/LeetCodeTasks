class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, visited, cur_i, cur_j):
            if cur_i >= len(grid) or cur_i < 0:
                return visited
            
            if cur_j >= len(grid[cur_i]) or cur_j < 0:
                return visited
            
            if grid[cur_i][cur_j] == '0':
                return visited
            
            if visited[cur_i][cur_j]:
                return visited


            visited[cur_i][cur_j] = True

            visited = dfs(grid, visited, cur_i, cur_j + 1)
            visited = dfs(grid, visited, cur_i - 1, cur_j)
            visited = dfs(grid, visited, cur_i, cur_j - 1)
            visited = dfs(grid, visited, cur_i + 1, cur_j)

            return visited
        
        visited = []
        for i in range(len(grid)):
            visited.append([False] * len(grid[i]))

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j] == '1':
                    island_count += 1
                    visited = dfs(grid, visited, i, j)
        
        return island_count
