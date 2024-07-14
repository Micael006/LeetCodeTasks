import random
class RandomizedSet:

    def __init__(self):
        self.data = dict()
        self.dupl = []

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.dupl.append(val)
            self.data[val] = len(self.dupl) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            idx = self.data[val]
            self.data[self.dupl[-1]] = idx
            self.dupl[idx], self.dupl[-1] = self.dupl[-1], self.dupl[idx]
            self.dupl.pop()
            del self.data[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.dupl)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()