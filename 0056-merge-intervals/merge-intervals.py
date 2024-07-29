class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0]
        answer = []

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            if cur_start <= end:
                end = max(end, cur_end)
            else:
                answer.append([start, end])
                start, end = cur_start, cur_end
        
        answer.append([start, end])

        return answer