import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        su=0
        nums=[-num for num in nums]
        heapq.heapify(nums)
        for i in range(k):
            big = -heapq.heappop(nums)
            su += big
            heapq.heappush(nums,-ceil(big/3))
        return su