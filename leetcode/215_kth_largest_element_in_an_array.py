import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []

        for i in nums:
            if len(heap) < k:
                heapq.heappush(heap, i)
            else:
                if heap[0] < i:
                    heapq.heapreplace(heap, i)
        
        return heap[0]