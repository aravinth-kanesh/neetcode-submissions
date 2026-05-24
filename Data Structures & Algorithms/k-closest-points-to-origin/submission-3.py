class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # max heap

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        while heap:
            _, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res