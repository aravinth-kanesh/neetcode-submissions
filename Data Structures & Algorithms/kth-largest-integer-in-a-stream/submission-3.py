class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        # min heap
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # push if heap smaller than k
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # pop and push
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]

        
