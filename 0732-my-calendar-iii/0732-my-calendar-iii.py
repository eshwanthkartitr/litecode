class MyCalendarThree:

    def __init__(self):
        '''Somehow map the intersection with the corresponding max intersection because when intersecting i can use the prev value like dp'''
        self.intersection=defaultdict(int)
        

    def book(self, start: int, end: int) -> int:
        self.intersection[start]+=1
        self.intersection[end]-=1
        ongoing = 0
        max_k = 0
        for time in sorted(self.intersection):
            ongoing += self.intersection[time]
            max_k = max(max_k,ongoing)
        return max_k
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)