class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = [0] * 10**6
        for i in range(len(nums)):
            count[nums[i]] += 1
        
        steps = 0
        for i in range(len(count)):
            if count[i] > 1:
                steps += count[i] - 1
                count[i + 1] += count[i] - 1
        return steps 