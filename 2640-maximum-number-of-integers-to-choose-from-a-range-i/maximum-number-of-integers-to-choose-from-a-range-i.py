class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        numbers = []
        banned = sorted(list(set(banned)))
        banned_index = 0
        for num in range(1, min(n + 1, maxSum + 1)):
            if banned_index < len(banned) and num == banned[banned_index]:
                banned_index += 1
                continue
            numbers.append(num)

        cur_sum = 0
        counter = 0
        for i in range(len(numbers)):
            if cur_sum + numbers[i] > maxSum:
                break
            cur_sum += numbers[i]
            counter += 1
            
        return counter