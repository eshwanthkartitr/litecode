from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        
        def dijkstra(start):
            min_heap = [(0, start)]
            distances = {i: float('inf') for i in range(n)}
            distances[start] = 0

            while min_heap:
                current_dist, current_node = heapq.heappop(min_heap)
                if current_dist > distances[current_node]:
                    continue
                for neighbor, weight in graph[current_node]:
                    distance = current_dist + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(min_heap, (distance, neighbor))
            return sum(1 for dist in distances.values() if dist <= distanceThreshold) - 1
        
        min_reachable_cities = float('inf')
        city_with_min_reach = -1
        for city in range(n):
            reachable_cities = dijkstra(city)
            if reachable_cities <= min_reachable_cities:
                if reachable_cities == min_reachable_cities:
                    city_with_min_reach = max(city_with_min_reach, city)
                else:
                    min_reachable_cities = reachable_cities
                    city_with_min_reach = city

        return city_with_min_reach
