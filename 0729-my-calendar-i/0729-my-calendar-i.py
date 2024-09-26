class Node():
    def __init__(self,start,end,left=None,right=None):
        self.start=start
        self.end=end
        self.left=left
        self.right=right

    def insert(self,start,end):
        if self.start < end and self.end > start:
            return False
        if self.start >= end:
            if self.right is None:
                self.right = Node(start,end)
                return True
            else:
                return self.right.insert(start,end)
        elif self.end <= start:
            if self.left is None:
                self.left=Node(start,end)
                return True
            else:
                return self.left.insert(start,end)
        return True

class MyCalendar:
    def __init__(self):
        self.start = None

    def book(self, start: int, end: int) -> bool:
        if not self.start:
            self.start = Node(start,end)
            return True
        else:
            return self.start.insert(start,end)
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)