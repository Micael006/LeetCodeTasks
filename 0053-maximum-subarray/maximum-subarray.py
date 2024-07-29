class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_pref = -(10**10)
        min_pref = 10**10
        pref = 0
        for i in range(len(nums)):
            pref += nums[i]
            max_pref = max(max_pref, pref, pref - min_pref)
            min_pref = min(min_pref, pref)
        return max_pref