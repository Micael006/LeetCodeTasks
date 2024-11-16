class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        answer = []
        for i in range(len(nums) - k + 1):
            stopped = False
            for j in range(i + 1, i + k):
                if nums[j] - nums[j - 1] != 1:
                    stopped = True
                    break
            answer.append(-1 if stopped else nums[i + k - 1])

        return answer