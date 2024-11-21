class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        visited = []
        for i in range(m):
            visited.append([0] * n)
        
        for row, col in walls + guards:
            visited[row][col] = -1
        
        for row, col in guards:
            for i in range(row - 1, -1, -1):
                if visited[i][col] == -1:
                    break
                visited[i][col] += 1
            for i in range(row + 1, m):
                if visited[i][col] == -1:
                    break
                visited[i][col] += 1
            for i in range(col - 1, -1, -1):
                if visited[row][i] == -1:
                    break
                visited[row][i] += 1
            for i in range(col + 1, n):
                if visited[row][i] == -1:
                    break
                visited[row][i] += 1
        
        answer = 0
        for row in range(m):
            for col in range(n):
                answer += visited[row][col] == 0
        
        return answer