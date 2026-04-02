class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap to store the distance between the origin and points
        heap = []

        # edge case
        if not points or k > len(points):
            return []

        # if this line is reached k is a valid number given the number
        # of points in the input array
        for x, y in points:
            # square root can be performed using ** in python
            # since origin is (0, 0), can just do root(x^2 + y^2)
            distance = ((x ** 2) + (y ** 2)) ** 0.5

            # push the original point to the heap as well (so it can
            # be extracted)
            heapq.heappush(heap, (distance, [x, y]))

        result = []

        # return only the points, not the distance
        for _ in range(k):
            distance, point = heapq.heappop(heap)
            result.append(point)

        return result

        