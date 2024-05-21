class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2**len(nums)):
            helper = str(bin(i))[2:].zfill(len(nums))
            new_subset = []
            for j in range(len(helper)):
                if helper[j] == '1':
                    new_subset.append(nums[j])
            if new_subset not in ans:
                ans.append(new_subset)
        return ans