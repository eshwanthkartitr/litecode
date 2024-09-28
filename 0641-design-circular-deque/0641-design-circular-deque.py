class MyCircularDeque:

    def __init__(self, k: int):
        self.re=[]
        self.k=k

    def insertFront(self, value: int) -> bool:
        if self.k > len(self.re):
            self.re=self.re[::-1]
            self.re.append(value)
            self.re=self.re[::-1]
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        if self.k > len(self.re):
            self.re.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.re)!=0:
            self.re.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.re)!=0:
            self.re.pop()
            return True
        else:
            return False

    def getFront(self) -> int:

        return self.re[0]

    def getRear(self) -> int:
        print(self.re)
        return self.re[-1]

    def isEmpty(self) -> bool:
        return len(self.re)==0

    def isFull(self) -> bool:
        return len(self.re)==self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getself.rear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()