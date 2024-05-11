import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(quality))])
        res = float('inf')
        min_heap = []
        total_quality = 0

        for ratio, q in workers:
            total_quality += q
            heapq.heappush(min_heap, -q)

            if len(min_heap) > k:
                total_quality += heapq.heappop(min_heap)

            if len(min_heap) == k:
                res = min(res, ratio * total_quality)

        return res