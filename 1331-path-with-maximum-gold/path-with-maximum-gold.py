class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(v, cur_i, cur_j, printed):
            new_v = []
            for i in range(len(v)):
                new_v.append(v[i][:])
            if cur_i < 0 or cur_i >= len(grid) or cur_j < 0 or cur_j >= len(grid[0]):
                return 0
            if grid[cur_i][cur_j] == 0 or v[cur_i][cur_j]:
                return 0
            val = grid[cur_i][cur_j]
            new_v[cur_i][cur_j] = True
            answer = val + max(dfs(new_v, cur_i - 1, cur_j, printed), dfs(new_v, cur_i, cur_j + 1, printed), dfs(new_v, cur_i + 1, cur_j, printed), dfs(new_v, cur_i, cur_j - 1, printed))
            #if(printed):
                #print(cur_i, cur_j, answer)
                #print(*new_v, sep='\n')
                #print()
            return answer
        
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                visited = []
                for k in range(len(grid)):
                    visited.append([False] * len(grid[i]))
                max_gold = max(max_gold, dfs(visited, i, j, True if i == 4 and j == 4 else False))
        return max_gold