class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        matrix = [[x for x in range(1, n + 1)]]
        for i in range(1, n):
            matrix.append([0] * n)
        
        cur_num = n + 1
        n -= 1
        cur_pos = [n, 0]
        cur_dir = 1

        while n > 0:
            for _ in range(2):
                for _ in range(n):
                    cur_pos = [cur_pos[0] + directions[cur_dir][0], cur_pos[1] + directions[cur_dir][1]]
                    matrix[cur_pos[1]][cur_pos[0]] = cur_num
                    cur_num += 1
                cur_dir = (cur_dir + 1) % len(directions)
            n -= 1
        
        return matrix