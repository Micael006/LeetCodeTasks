class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = dict()
        prefix[0] = 1
        cur_pref = 0
        count = 0
        for i in range(len(nums)):
            cur_pref = (cur_pref + nums[i]) % k
            count += prefix.get(cur_pref, 0)
            prefix[cur_pref] = prefix.get(cur_pref, 0) + 1
        return count
            
                