from functools import reduce
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(1, 2**n):
            xor = 0
            for j in range(n):
                if i & (1 << j):
                    xor ^= nums[j]
            count += xor
            #arr = [nums[x] for x in range(len(helper)) if helper[x] == '1']
            #count += reduce(lambda x, y: x ^ y, arr, 0)
            #print(helper, arr)
        return count