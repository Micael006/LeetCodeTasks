class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        mn, mx = min(heights), max(heights)
        keys = [0] * (mx - mn + 1)
        for i in range(len(heights)):
            keys[heights[i] - mn] += 1
        expected = []
        for i in range(len(keys)):
            expected += [mn + i] * keys[i]
        count = 0
        for i in range(len(heights)):
            count += expected[i] != heights[i]
        return count
