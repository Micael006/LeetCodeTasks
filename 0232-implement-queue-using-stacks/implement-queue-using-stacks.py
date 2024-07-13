class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        helper = []

        for i in range(len(self.data)):
            helper.append(self.data.pop())
        
        elem = helper.pop()
        
        for i in range(len(helper)):
            self.data.append(helper.pop())
        
        return elem

    def peek(self) -> int:
        helper = []

        for i in range(len(self.data)):
            helper.append(self.data.pop())
        
        elem = helper[-1]
        
        for i in range(len(helper)):
            self.data.append(helper.pop())
        
        return elem

    def empty(self) -> bool:
        return len(self.data) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()