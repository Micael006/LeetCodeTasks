class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_non_val = len(nums) - 1
        pointer = 0
        while pointer <= last_non_val:
            if nums[pointer] == val:
                nums[pointer], nums[last_non_val] = nums[last_non_val], nums[pointer]
                last_non_val -= 1
                continue
            pointer += 1
        return last_non_val + 1