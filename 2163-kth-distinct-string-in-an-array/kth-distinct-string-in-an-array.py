class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distincts = dict()
        for i in range(len(arr)):
            if arr[i] not in distincts:
                distincts[arr[i]] = [i, 0]
            distincts[arr[i]][1] += 1
        
        ordered = [[key, distincts[key][0]] for key in distincts if distincts[key][1] == 1]
        ordered.sort(key=lambda tup: tup[1])

        if k <= len(ordered):
            return ordered[k - 1][0]
        return ''