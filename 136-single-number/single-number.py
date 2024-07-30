class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            answer ^= nums[i]
        
        return answer