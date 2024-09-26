class MyCalendar:

    def __init__(self):
        self.re=[]

    def book(self, start: int, end: int) -> bool:
        if self.re==[]:
            self.re.append((start,end))
            return True
        else:
            for i in self.re:
                if i[1] > start and end>i[0]:
                    return False
            self.re.append((start,end))
            print((start,end))
            return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)