class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        cur_dir = 0
        cur_step = 1
        answer = [[rStart, cStart]]
        while cur_step < 2 * max(cols, rows):
            for i in range(2):
                for j in range(cur_step):
                    rStart += directions[cur_dir][1]
                    cStart += directions[cur_dir][0]
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        answer.append([rStart, cStart])
                cur_dir = (cur_dir + 1) % len(directions)
            cur_step += 1
        return answer