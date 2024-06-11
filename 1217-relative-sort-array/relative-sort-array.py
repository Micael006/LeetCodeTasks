class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        keys = [0] * 1001
        start_arr = []
        end_arr = []
        for elem in arr1:
            keys[elem] += 1
        for i in range(len(arr2)):
            start_arr += [arr2[i]] * keys[arr2[i]]
            keys[arr2[i]] = 0
        for i in range(len(keys)):
            end_arr += [i] * keys[i]

        return start_arr + end_arr