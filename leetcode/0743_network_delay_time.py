from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = defaultdict(list)
        for i, j, time in times:
            if i != j:
                adj_list[i].append((j, time))
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        visited = set()
        pq = [(0, k)]
        while pq:
            curr_dist, i = heapq.heappop(pq)
            if curr_dist > dist[i]:
                continue
            for neighbor, time in adj_list[i]:
                if dist[neighbor] > dist[i] + time:
                    dist[neighbor] = dist[i] + time
                    heapq.heappush(pq, (dist[i] + time, neighbor))
        
        max_time = max(dist[1:])
        return max_time if max_time != float('inf') else -1
        


        