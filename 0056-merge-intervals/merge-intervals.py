class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0]
        print(start, end)
        answer = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                answer.append([start, end])
                start, end = intervals[i]
        answer.append([start, end])
        return answer