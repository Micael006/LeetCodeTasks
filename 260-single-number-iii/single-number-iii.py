class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cur = 0
        for i in range(len(nums)):
            cur ^= nums[i]
        n = 0
        while cur % 2 == 0:
            cur = cur >> 1
            n += 1
        cur0 = 0
        cur1 = 0
        for i in range(len(nums)):
            if nums[i] ^ 2**n > nums[i]:
                cur0 ^= nums[i]
            else:
                cur1 ^= nums[i]
        return [cur0, cur1]

