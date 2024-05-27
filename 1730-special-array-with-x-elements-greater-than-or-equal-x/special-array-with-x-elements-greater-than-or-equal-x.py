class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        print(len(nums))
        pos = 0
        for i in range(nums[-1] + 1):
            while i > nums[pos] and pos < len(nums):
                pos += 1
            if pos == len(nums):
                break
            if i == len(nums) - pos:
                return i
        return -1