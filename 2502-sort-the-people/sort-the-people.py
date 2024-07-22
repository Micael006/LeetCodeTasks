class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        connections = [(heights[i], names[i]) for i in range(len(names))]
        connections.sort(reverse=True)
        return [x[1] for x in connections]