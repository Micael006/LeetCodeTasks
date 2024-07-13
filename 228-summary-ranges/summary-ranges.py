class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        ans = []
        l, r = 0, 1
        cur_num = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] - cur_num > 1:
                if r - l == 1:
                    ans.append(str(nums[l]))
                else:
                    ans.append(f"{nums[l]}->{nums[r - 1]}")
                l = i
                r = i
            
            cur_num = nums[i]
            r += 1
        
        if r - l == 1:
            ans.append(str(nums[l]))
        else:
            ans.append(f"{nums[l]}->{nums[r - 1]}")
        
        return ans