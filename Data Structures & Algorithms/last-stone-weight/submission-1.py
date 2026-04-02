class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        heap = [-weight for weight in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:
            heavier = -heapq.heappop(heap)
            lighter = -heapq.heappop(heap)

            # the second popped stone is lighter than the first
            if heavier != lighter:
                # push heavier - lighter weight stone to the heap
                heapq.heappush(heap, -(heavier - lighter))

        # return 0 if the heap is empty after the simulation
        return -heap[0] if heap else 0