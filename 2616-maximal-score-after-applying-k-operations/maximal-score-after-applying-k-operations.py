class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for elem in nums:
            heapq.heappush(heap, -elem)
        
        answer = 0
        for i in range(k):
            cur = abs(heapq.heappop(heap))
            answer += cur
            cur = math.ceil(cur / 3)
            heapq.heappush(heap, -cur)
        
        return answer
