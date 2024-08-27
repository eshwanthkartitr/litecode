import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        mp=defaultdict(list)
        for idx, (u, v) in enumerate(edges):
            mp[u].append([v, succProb[idx]])
            mp[v].append([u, succProb[idx]])
        q=[(-1,start_node)]
        visited=set()
        mn=0
        while q:
            prob,curr = heapq.heappop(q)
            prob=-prob
            if curr in visited:
                continue
            visited.add(curr)
            if curr==end_node:
                return prob
            for i in mp[curr]:
                if i[0] not in visited:
                    heapq.heappush(q,(-(i[1]*prob),i[0]))
        return 0.0