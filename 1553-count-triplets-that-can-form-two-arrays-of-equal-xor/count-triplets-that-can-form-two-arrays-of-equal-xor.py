class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        table = dict()
        for i in range(len(arr)):
            helper = arr[i]
            table[(i, i)] = helper
            for j in range(i + 1, len(arr)):
                helper ^= arr[j]
                table[(i, j)] = helper

        count = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    a = table[(i, j - 1)]
                    b = table[(j, k)]
                    if a == b:
                        count += 1
                    '''a = arr[i]
                    for z in range(i + 1, j):
                        a ^= arr[z]
                    b = arr[j]
                    for z in range(j + 1, k + 1):
                        b ^= arr[z]
                    if a==b:
                        count += 1'''
        return count
