class Solution:
    def findScore(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        used = [False] * len(nums)
        nums = [x for x in enumerate(nums)]
        # Индекс, значение
        nums.sort(key=lambda x: (x[1], x[0]))
        answer = 0
        for i in range(len(nums)):
            if used[nums[i][0]]:
                continue
            answer += nums[i][1]
            used[nums[i][0]] = True
            if nums[i][0] > 0:
                used[nums[i][0] - 1] = True
            if nums[i][0] < len(nums) - 1:
                used[nums[i][0] + 1] = True
        
        return answer