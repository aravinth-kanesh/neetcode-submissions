import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # max heap implementation
        # push k differences to the heap
        # only push consequent differences if within max diff

        # need to store the nums as well
        heap = [(-abs(x - num), num) for num in arr[:k]]
        heapq.heapify(heap)

        for num in arr[k:]:
            diff = -abs(x - num)
            
            if diff > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (diff, num))
            
        res = []
        
        while heap:
            diff, num = heapq.heappop(heap)
            res.append(num)

        res.sort()
        return res