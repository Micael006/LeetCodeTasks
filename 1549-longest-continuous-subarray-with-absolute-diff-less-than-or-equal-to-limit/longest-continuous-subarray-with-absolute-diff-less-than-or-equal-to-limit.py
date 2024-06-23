class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        l = 0
        answer = 0
        for r in range(len(nums)):
            while len(max_deque) > 0 and max_deque[-1] < nums[r]:
                max_deque.pop()
            max_deque.append(nums[r])

            while len(min_deque) > 0 and min_deque[-1] > nums[r]:
                min_deque.pop()
            min_deque.append(nums[r])

            while abs(max_deque[0] - min_deque[0]) > limit:
                if nums[l] == max_deque[0]:
                    max_deque.popleft()
                if nums[l] == min_deque[0]:
                    min_deque.popleft()
                l += 1
            
            answer = max(r - l + 1, answer)
        
        return answer