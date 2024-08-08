class OrderedStream:

    def __init__(self, n: int):
        self.mp=defaultdict(str)
        self.point = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.mp[idKey] = value
        re = []
        while self.point+1 in self.mp:
            self.point+=1
            re.append(self.mp[self.point])
        return re


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)