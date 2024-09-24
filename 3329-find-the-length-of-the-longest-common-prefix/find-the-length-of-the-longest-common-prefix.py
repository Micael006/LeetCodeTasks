class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        helper = set()
        for number in arr1:
            for i in range(1, len(str(number)) + 1):
                helper.add(str(number)[:i])
        
        answer = 0
        for number in arr2:
            for i in range(1, len(str(number)) + 1):
                if str(number)[:i] in helper:
                    answer = max(answer, i)
        
        return answer