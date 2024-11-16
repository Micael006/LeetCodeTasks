class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        answer = []
        window = deque([])
        for i in range(len(nums)):
            if len(window) == k:
                window.popleft()
            if len(window) > 0 and nums[i] - window[-1] != 1:
                window = deque([])
            window.append(nums[i])
            if len(window) == k:
                answer.append(window[-1])
            else:
                answer.append(-1)

        return answer[k - 1:]