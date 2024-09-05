class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        full_sum = mean * (m + n) - sum(rolls)
        if full_sum < n or full_sum > 6 * n:
            return []
        
        remains = full_sum - n
        answer = [1] * n
        index = 0
        while remains > 0 and index < len(answer):
            cur = min(5, remains)
            remains -= cur
            answer[index] += cur
            index += 1
        if remains > 0:
            return []
        return answer