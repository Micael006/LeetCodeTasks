class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(matrix)):
            cur_min = min(matrix[i])
            j = matrix[i].index(cur_min)
            cur_max = max([matrix[z][j] for z in range(len(matrix))])
            
            if cur_max == cur_min:
                ans.append(cur_min)
        
        return ans