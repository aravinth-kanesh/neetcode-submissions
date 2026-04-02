class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        if not points or k > len(points):
            return heap

        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(heap, (-distance, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

        return [point for distance, point in heap]