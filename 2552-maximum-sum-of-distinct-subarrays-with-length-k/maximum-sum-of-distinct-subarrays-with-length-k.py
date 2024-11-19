class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = deque()
        window_sum = 0
        helper = dict()
        for i in range(k - 1):
            window.append(nums[i])
            window_sum += nums[i]
            helper[nums[i]] = helper.get(nums[i], 0) + 1
        
        max_sum = 0

        for i in range(k - 1, len(nums)):
            window.append(nums[i])
            window_sum += nums[i]
            helper[nums[i]] = helper.get(nums[i], 0) + 1

            if len(helper.keys()) == k:
                max_sum = max(max_sum, window_sum)
            
            to_delete = window.popleft()
            window_sum -= to_delete
            helper[to_delete] -= 1
            if helper[to_delete] == 0:
                del helper[to_delete]
        
        return max_sum