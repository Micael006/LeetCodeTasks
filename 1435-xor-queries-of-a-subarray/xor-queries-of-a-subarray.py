class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        prefix = [0]
        cur = 0
        for elem in arr:
            cur ^= elem
            prefix.append(cur)
        
        for query in queries:
            answer.append(prefix[query[1] + 1] ^ prefix[query[0]])
        
        return answer
