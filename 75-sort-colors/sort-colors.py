class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counters = [0, 0, 0]
        for i in range(len(nums)):
            counters[nums[i]] += 1
        print(counters)
        nums[:counters[0]] = [0] * counters[0]
        nums[counters[0]:counters[0] + counters[1]] = [1] * counters[1]
        nums[counters[0] + counters[1]:] = [2] * counters[2]
        