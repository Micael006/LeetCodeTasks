class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = dict()
        cur_pref = 0
        prefix[0] = 1
        answer = 0
        for i in range(len(nums)):
            cur_pref += nums[i]
            if (cur_pref - k) in prefix:
                answer += prefix[cur_pref - k]
            prefix[cur_pref] = prefix.get(cur_pref, 0) + 1
        
        return answer