class CustomStack:

    def __init__(self, maxSize: int):
        self.re=[]
        self.mx = maxSize

    def push(self, x: int) -> None:
        if len(self.re) == self.mx:
            return 
        print(self.re)
        self.re.append(x)

    def pop(self) -> int:
        print(self.re)

        if len(self.re)!=0:
            return self.re.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        print(self.re)

        for i in range(min(k,len(self.re))):
            self.re[i] += val
        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)