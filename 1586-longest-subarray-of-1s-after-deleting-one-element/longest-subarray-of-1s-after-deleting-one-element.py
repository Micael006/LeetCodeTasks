class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        window = deque()
        answer = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                continue
            
            if len(window) > 0:
                answer = max(answer, i - l - 1)
                l = window.popleft() + 1
            
            window.append(i)
        
        answer = max(answer, len(nums) - l - 1)
        
        return max(0, answer)