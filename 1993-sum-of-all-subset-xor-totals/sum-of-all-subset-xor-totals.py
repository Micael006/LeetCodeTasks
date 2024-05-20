from functools import reduce
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, 2**len(nums)):
            helper = bin(i)[2:][::-1]
            arr = [nums[x] for x in range(len(helper)) if helper[x] == '1']
            count += reduce(lambda x, y: x ^ y, arr, 0)
            print(helper, arr)
        return count