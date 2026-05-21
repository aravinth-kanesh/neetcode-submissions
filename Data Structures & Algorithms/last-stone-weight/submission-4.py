class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-w for w in stones]
        heapq.heapify(heap)
        
        # must have two or more stones for the simulation
        # to continue
        while len(heap) >= 2:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)

            if x > y:
                heapq.heappush(heap, -(x - y))

        return -heap[0] if heap else 0