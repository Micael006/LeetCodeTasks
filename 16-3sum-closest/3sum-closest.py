class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = 10**20
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(cur_sum - target) < abs(answer - target):
                    answer = cur_sum
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    return cur_sum
        
        return answer
