class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key=lambda x:x[0])
        heap=[]
        for start,end in intervals:
            if heap and heap[0]<start:
                heapq.heappop(heap)
            heapq.heappush(heap,end)
        return len(heap)
            