class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            if d.get(target - nums[i]) is None:
                d[nums[i]] = i
            else:
                return [d[target - nums[i]], i]
        