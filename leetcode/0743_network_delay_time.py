from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Approach: use Dijkstra's algorithm to compute the shortest distance
        # from k to all other nodes in the graph

        # convert list of edges into an adjacency list
        adj_list = defaultdict(list)
        for i, j, time in times:
            # an edge to itself isn't relevant here
            if i != j:
                adj_list[i].append((j, time))

        # keep a running list of the minimum distance from k to each node
        dist = [float('inf')] * (n+1)
        # the distance from k to itself is 0
        dist[k] = 0

        # a priority queue to return the most promising (node, min_distance)
        pq = [(0, k)]
        while pq:
            curr_dist, i = heapq.heappop(pq)
            if curr_dist > dist[i]:
                continue

            # for each neighbor of the current node
            for neighbor, time in adj_list[i]:
                # check if we can do better than current min distance to the neighbor by going
                # from i to the neighbor
                if dist[neighbor] > dist[i] + time:
                    dist[neighbor] = dist[i] + time
                    heapq.heappush(pq, (dist[i] + time, neighbor))
        
        # the max time is the rate limiting time to reach all nodes
        max_time = max(dist[1:])
        
        return max_time if max_time != float('inf') else -1
        


        