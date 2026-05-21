class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a max heap
        heap = [-weight for weight in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)
            
            if x < y:
                heapq.heappush(heap, -(y - x))
            elif y < x:
                heapq.heappush(heap, -(x - y))

            print(heap)

        return -heap[0] if heap else 0

