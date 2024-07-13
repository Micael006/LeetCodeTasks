class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur_pos] = nums[i]
                cur_pos += 1
        
        for i in range(cur_pos, len(nums)):
            nums[i] = 0