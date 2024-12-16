class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))
        
        for _ in range(k):
            cur, cur_i = heapq.heappop(heap)
            heapq.heappush(heap, (cur * multiplier, cur_i))
        
        while heap:
            cur, cur_i = heapq.heappop(heap)
            nums[cur_i] = cur
        
        return nums