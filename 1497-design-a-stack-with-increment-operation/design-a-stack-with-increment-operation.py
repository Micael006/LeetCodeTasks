class CustomStack:

    def __init__(self, maxSize: int):
        self.data = []
        self.capacity = maxSize

    def push(self, x: int) -> None:
        if len(self.data) < self.capacity:
            self.data.append(x)

    def pop(self) -> int:
        if len(self.data) > 0:
            return self.data.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        helper = []
        while len(self.data) > 0:
            helper.append(self.data.pop())
        
        for i in range(min(len(helper), k)):
            self.data.append(helper.pop() + val)
        
        while len(helper) > 0:
            self.data.append(helper.pop())


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)