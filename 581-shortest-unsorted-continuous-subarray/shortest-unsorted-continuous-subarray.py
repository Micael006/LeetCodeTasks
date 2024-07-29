class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l, r = 10**10, -10**10
        max_val, min_val = -10**10, 10**10

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= min_val:
                min_val = nums[i]
            else:
                l = i
        
        for i in range(len(nums)):
            if nums[i] >= max_val:
                max_val = nums[i]
            else:
                r = i
        
        return max(0, r - l + 1)