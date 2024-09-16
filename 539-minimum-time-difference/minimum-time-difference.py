class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        helper = []
        for point in timePoints:
            hours, minutes = point.split(':')
            helper.append(int(hours) * 60 + int(minutes))
        
        helper.sort()
        answer = 1440

        for i in range(len(helper) - 2, -2, -1):
            cur = abs(helper[i] - helper[i + 1])
            answer = min(answer, cur, 1440 - cur)

        return answer     