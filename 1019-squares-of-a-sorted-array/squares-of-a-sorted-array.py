class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_arr = []
        pos_idx = -1
        neg_idx = -1
        for i in range(len(nums)):
            if nums[i] >= 0:
                pos_idx = i
                neg_idx = i - 1
                break
        
        if pos_idx == -1:
            neg_idx = len(nums) - 1
            pos_idx = len(nums)
        
        ans = []
        while pos_idx < len(nums) and neg_idx > -1:
            if nums[pos_idx] < abs(nums[neg_idx]):
                ans.append(nums[pos_idx]**2)
                pos_idx += 1
            else:
                ans.append(nums[neg_idx]**2)
                neg_idx -= 1

        while pos_idx < len(nums):
            ans.append(nums[pos_idx]**2)
            pos_idx += 1
        
        while neg_idx > -1:
            ans.append(nums[neg_idx]**2)
            neg_idx -= 1
        
        return ans
