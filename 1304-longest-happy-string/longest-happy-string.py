class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        
        answer = ""
        while heap:
            count, character = heapq.heappop(heap)
            if len(answer) >= 2 and answer[-1] == answer[-2] == character:
                if not heap:
                    break

                temp = heapq.heappop(heap)
                heapq.heappush(heap, (count, character))
                count, character = temp
            
            count += 1
            answer += character

            if count < 0:
                heapq.heappush(heap, (count, character))
        
        return answer


