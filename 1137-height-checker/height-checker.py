class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights[:]
        expected.sort()
        count = 0
        for i in range(len(heights)):
            count += expected[i] != heights[i]
        return count
