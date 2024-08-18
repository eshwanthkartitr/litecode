# Neetcode help
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr=[1]
        vist=set()
        for i in range(n-1):
            val = heapq.heappop(arr)
            for j in [2,3,5]:
                if val*j not in vist:
                    heapq.heappush(arr,val*j)
                    vist.add(val*j)
        return min(arr) 