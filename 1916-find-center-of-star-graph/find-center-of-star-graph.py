class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first, last = edges[0]
        if first in edges[1]:
            return first
        return last