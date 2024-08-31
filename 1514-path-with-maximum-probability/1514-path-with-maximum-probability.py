import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        mp=defaultdict(list)
        for i,(j,k) in enumerate(edges):
            mp[j].append((k,succProb[i]))
            mp[k].append((j,succProb[i]))
        q=[(-1,start_node)]
        heapify(q)
        visited=set()
        while q:
            print(q)
            prob,node = heapq.heappop(q)
            prob = -prob
            if node in visited:
                continue
            visited.add(node)
            if node == end_node:
                return prob
            for j,k in mp[node]:
                heapq.heappush(q,(-k*prob,j))
        return 0.0