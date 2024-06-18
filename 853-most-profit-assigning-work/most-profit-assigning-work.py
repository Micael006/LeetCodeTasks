class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        prefix = [0] * 10**5
        for i in range(len(difficulty)):
            prefix[difficulty[i]] = max(prefix[difficulty[i]], profit[i])
        for i in range(1, len(prefix)):
            prefix[i] = max(prefix[i], prefix[i - 1])
        answer = 0
        for i in range(len(worker)):
            answer += prefix[worker[i]]
        return answer