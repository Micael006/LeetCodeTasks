class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = []
        for i in range(len(box)):
            rows.append([])
            sector_start = 0
            stone_count = 0
            for j in range(len(box[i])):
                if box[i][j] == '*':
                    rows[-1].append([sector_start, j, stone_count])
                    stone_count = 0
                    sector_start = j + 1
                elif box[i][j] == '#':
                    stone_count += 1
            
            if sector_start < len(box[i]):
                rows[-1].append([sector_start, len(box[i]), stone_count])
        
        answer = []
        for i in range(len(box[0])):
            answer.append(['.'] * len(box))
        
        for i in range(len(rows)):
            for s_start, s_end, s_count in rows[i]:
                for offset in range(s_count):
                    answer[s_end - 1 - offset][len(box) - 1 - i] = '#'
                if s_end < len(answer):
                    answer[s_end][len(box) - 1 - i] = '*'
        
        return answer

