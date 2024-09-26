class MyCalendar:

    def __init__(self):
        self.data = []

    def book(self, start: int, end: int) -> bool:
        checked = True
        for item in self.data:
            if max(start, item[0]) <= min(end - 1, item[1]):
                checked = False
                break
        
        if checked:
            self.data.append([start, end - 1])
        
        return checked


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)