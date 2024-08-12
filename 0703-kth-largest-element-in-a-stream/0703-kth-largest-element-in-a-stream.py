class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.li=nums
        self.k=k
        self.li.sort()

    def add(self, val: int) -> int:
        re=[]
        fl=1
        for i in range(len(self.li)):
            if self.li[i]>val:
                re = self.li[:i]+[val]+self.li[i:]
                fl=0
                break
        if fl == 1:
            re = self.li+[val]
        self.li=re
        return self.li[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)