class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = dict()
        for i in range(len(nums)):
            if check.get(target - nums[i]) is not None:
                return([check[target - nums[i]], i])
            check[nums[i]] = i