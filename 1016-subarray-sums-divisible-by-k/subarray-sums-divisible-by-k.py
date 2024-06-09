class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = dict()
        prefix[0] = 1
        cur_prefix = 0
        count = 0
        for i in range(len(nums)):
            cur_prefix += nums[i]
            if prefix.get(cur_prefix % k):
                count += prefix[cur_prefix % k]
            prefix[cur_prefix % k] = prefix.get(cur_prefix % k, 0) + 1
        return count
                