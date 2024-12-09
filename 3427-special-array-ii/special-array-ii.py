class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]*len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + (nums[i] % 2 == nums[i-1] % 2)
        
        answer = []
        for left, right in queries:
            answer.append((prefix[right] - (prefix[left] if left > 0 else 0)) == 0)

        return answer
