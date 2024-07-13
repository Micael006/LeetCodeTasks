class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        dict_a, dict_b = dict(), dict()
        common_count = 0
        ans = []
        for i in range(len(A)):
            if A[i] == B[i]:
                common_count += 1
            else:
                if dict_b.get(A[i], 0) > 0:
                    common_count += 1
                    dict_b[A[i]] -= 1
                else:
                    dict_a[A[i]] = dict_a.get(A[i], 0) + 1
                
                if dict_a.get(B[i], 0) > 0:
                    common_count  += 1
                    dict_a[B[i]] -= 1
                else:
                    dict_b[B[i]] = dict_b.get(B[i], 0) + 1
            ans.append(common_count)
        
        return ans