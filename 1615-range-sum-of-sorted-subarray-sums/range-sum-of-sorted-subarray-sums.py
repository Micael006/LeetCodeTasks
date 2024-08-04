class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        all_sums = []
        for i in range(len(nums)):
            cur_sum = nums[i]
            all_sums.append(cur_sum)
            for j in range(i + 1, len(nums)):
                cur_sum += nums[j]
                all_sums.append(cur_sum)
        
        return sum(sorted(all_sums)[left - 1: right]) % (10**9 + 7)