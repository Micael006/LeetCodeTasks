class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        min_cost = float("inf")
        cur_quality_sum = 0
        ratio_list = []

        for i in range(n):
            heappush(ratio_list, (wage[i] / quality[i], quality[i]))
        
        check = []

        for i in range(n):
            ratio, cur_quality = heappop(ratio_list)
            cur_quality_sum += cur_quality
            heappush(check, -cur_quality)

            if len(check) > k:
                cur_quality_sum += heappop(check)
            
            if len(check) == k:
                min_cost = min(min_cost, cur_quality_sum * ratio)
            
        return min_cost