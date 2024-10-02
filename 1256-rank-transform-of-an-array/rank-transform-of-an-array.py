class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        helper = dict()
        rank = 1
        for elem in sorted(list(set(arr))):
            helper[elem] = rank
            rank += 1
        
        return [helper[x] for x in arr]