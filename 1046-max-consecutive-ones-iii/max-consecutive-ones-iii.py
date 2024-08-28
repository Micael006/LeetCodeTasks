class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        answer = 0
        helper = deque()
        start = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if len(helper) < k:
                    helper.append(i)
                else:
                    answer = max(answer, i - start)
                    if len(helper) > 0:
                        start = helper.popleft() + 1
                        helper.append(i)
                    else:
                        start = i + 1
        return max(answer, len(nums) - start)