class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: int(''.join([str(mapping[int(elem)]) for elem in str(x)])))