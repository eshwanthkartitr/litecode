import heapq
class Solution:
    def maxAverageRatio(self, nums: List[List[int]], wan: int) -> float:
        n = len(nums)
        heap=[]
        for a,b in nums:
            gain  = ((a+1)/(b+1)) - (a/b)
            heapq.heappush(heap,(-gain,a,b))

        for _ in range(wan):
            _,a,b = heapq.heappop(heap)
            a+=1
            b+=1
            new_gain  = ((a+1)/(b+1)) - (a/b)
            heapq.heappush(heap,(-new_gain,a,b))
        
        return sum([a/b for _,a,b in heap]) / n