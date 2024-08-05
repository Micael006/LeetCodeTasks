class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distincts = dict()
        for i in range(len(arr)):
            distincts[arr[i]] = distincts.get(arr[i], 0) + 1

        cur_k = 1
        for i in range(len(arr)):
            if distincts[arr[i]] == 1:
                if cur_k == k:
                    return arr[i]
                cur_k += 1
        
        return ''
            