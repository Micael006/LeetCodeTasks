import math

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = dict()
        prefix[nums[0] % k] = 0
        cur_pref = nums[0] % k
        for i in range(1, len(nums)):
            cur_pref = (cur_pref + nums[i]) % k
            if (cur_pref == 0) or (prefix.get(cur_pref, -1) > -1 and prefix[cur_pref] <= i - 2):
                return True
            prefix[cur_pref] = min(prefix.get(cur_pref, len(nums)), i)

        return False

            
        
         