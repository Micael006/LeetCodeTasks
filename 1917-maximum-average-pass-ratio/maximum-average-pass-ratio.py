class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for i in range(len(classes)):
            pass_mark, total = classes[i]
            cur = pass_mark / total
            increase = (pass_mark + 1) / (total + 1) - cur
            heapq.heappush(heap, (-increase, i))
         
        for i in range(extraStudents):
            cur_increase, cur_index = heapq.heappop(heap)
            classes[cur_index][0] += 1
            classes[cur_index][1] += 1
            pass_mark, total = classes[cur_index]
            cur = pass_mark / total
            increase = (pass_mark + 1) / (total + 1) - cur
            heapq.heappush(heap, (-increase, cur_index))
        
        answer = sum([x[0] / x[1] for x in classes]) / len(classes)
        return answer