class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        if l >= len(nums):
            return [-1, -1]
        
        if nums[l] != target:
            return [-1, -1]
        
        start = l
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target + 1:
                l = m + 1
            else:
                r = m - 1
        
        return [start, max(start, l - 1)]