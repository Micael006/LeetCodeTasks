class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if target + 1 <= matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        
        if not (0 <= l - 1 < len(matrix)):
            return False
        
        string_index = l - 1
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if target <= matrix[string_index][m]:
                r = m - 1
            else:
                l = m + 1
        
        if 0 <= l < len(matrix[0]):
            return matrix[string_index][l] == target
        
        return False