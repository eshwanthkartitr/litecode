class ProductOfNumbers:

    def __init__(self):
        self.re=[1]
        self.pt=1

    def add(self, num: int) -> None:
        if num == 0:
            self.re=[1]
            self.pt=1
        else:
            self.re.append(self.re[-1]*num)
            self.pt+=1

    def getProduct(self, k: int) -> int:
        if k >= self.pt:
            return 0
        return self.re[-1]//self.re[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)