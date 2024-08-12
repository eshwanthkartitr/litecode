class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.li=nums
        self.k=k

    def add(self, val: int) -> int:
        self.li.append(val)
        self.li.sort()
        return self.li[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)