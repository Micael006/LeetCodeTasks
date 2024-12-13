import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-x for x in gifts]
        heapq.heapify(heap)
        for i in range(k):
            cur = abs(heapq.heappop(heap))
            heapq.heappush(heap, -math.floor(cur**0.5))
        
        return -sum(heap)
