class MyCalendarTwo:
    def __init__(self):
        self.events = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.events[start] += 1
        self.events[end] -= 1
        
        active_bookings = 0
        
        for time in sorted(self.events.keys()):
            active_bookings += self.events[time]
            
            if active_bookings >= 3:
                self.events[start] -= 1
                self.events[end] += 1
                
                if self.events[start] == 0:
                    del self.events[start]
                if self.events[end] == 0:
                    del self.events[end]
                
                return False
            
            if time > end:
                break
        
        return True