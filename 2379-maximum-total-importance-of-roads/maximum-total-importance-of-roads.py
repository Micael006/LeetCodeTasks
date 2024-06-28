class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = dict()
        for i in range(len(roads)):
            counter[roads[i][0]] = counter.get(roads[i][0], 0) + 1
            counter[roads[i][1]] = counter.get(roads[i][1], 0) + 1
        result = list(counter.values())
        result.sort(reverse=True)
        ans = 0
        for city in result:
            ans += n * city
            n -= 1
        return ans