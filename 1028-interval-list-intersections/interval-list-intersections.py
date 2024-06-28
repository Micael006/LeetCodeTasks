class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) * len(secondList) == 0:
            return []
        result = []
        last_second = 0
        for first in firstList:
            while last_second < len(secondList) and secondList[last_second][1] < first[0]:
                last_second += 1
            for second in secondList[last_second:]:
                if second[0] > first[1]:
                    break
                elif second[0] <= first[0] <= second[1]:
                    result.append([first[0], min(first[1], second[1])])
                elif second[0] <= first[1] <= second[1]:
                    result.append([max(second[0], first[0]), first[1]])
                elif first[0] <= second[0] <= first[1]:
                    result.append([second[0], min(second[1], first[1])])
                elif first[0] <= second[1] <= first[1]:
                    result.append([max(first[0], second[0]), second[1]])
        
        return result
                
