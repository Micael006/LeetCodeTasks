class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                product *= nums[i]
        
        if zero_count > 1:
            product = 0
        
        ans = []
        for i in range(len(nums)):
            if nums[i] != 0 and zero_count == 0:
                ans.append(int(product / nums[i]))
            elif nums[i] != 0 and zero_count > 0:
                ans.append(0)
            elif nums[i] == 0 and zero_count == 1:
                ans.append(product)
            elif nums[i] == 0 and zero_count > 1:
                ans.append(0)
        
        return ans