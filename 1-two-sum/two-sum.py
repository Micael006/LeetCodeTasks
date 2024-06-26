class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = dict()
        for i in range(len(nums)):
            if check.get(target - nums[i], None) is not None:
                return [i, check[target - nums[i]]]
            check[nums[i]] = i