class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        keys = [0] * 1001
        for elem in arr1:
            keys[elem] += 1
        for elem in arr2:
            keys[elem] *= -1
        start_arr = []
        end_arr = []
        for i in range(len(keys)):
            if keys[i] >= 0:
                end_arr += [i] * keys[i]
        for i in range(len(arr2)):
            start_arr += [arr2[i]] * -keys[arr2[i]]
        #print(start_arr)
        #print(end_arr)
        return start_arr + end_arr