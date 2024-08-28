class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        to_check = []
        visited = []
        for i in range(len(grid2)):
            visited.append([False] * len(grid2[0]))
        sub_counter = 0
        def dfs(cur_i, cur_j):
            if not (0 <= cur_i < len(grid2) and 0 <= cur_j < len(grid2[0])):
                return
            if visited[cur_i][cur_j]:
                return
            visited[cur_i][cur_j] = True
            if grid2[cur_i][cur_j] == 1:
                to_check.append([cur_i, cur_j])
                dfs(cur_i, cur_j + 1)
                dfs(cur_i - 1, cur_j)
                dfs(cur_i, cur_j - 1)
                dfs(cur_i + 1, cur_j)
        
        def check_sub(to_check):
            while len(to_check) > 0:
                pos = to_check.pop()
                if grid1[pos[0]][pos[1]] == 0:
                    return 0
            return 1

        for i in range(len(grid2)):
            for j in range(len(grid2[i])):
                if grid2[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)
                    sub_counter += check_sub(to_check)
                    to_check = []
        
        return sub_counter