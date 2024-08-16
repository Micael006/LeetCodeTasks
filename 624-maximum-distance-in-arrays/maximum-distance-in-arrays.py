class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort(key=lambda x: x[0])
        answer = 0
        for i in range(1, len(arrays)):
                answer = max(abs(arrays[0][-1] - arrays[i][0]), abs(arrays[i][-1] - arrays[0][0]), answer)
        
        return answer