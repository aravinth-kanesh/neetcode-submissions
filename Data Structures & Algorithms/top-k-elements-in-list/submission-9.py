class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []

        for num, occ in freq.items():
            heapq.heappush(heap, (occ, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for occ, num in heap]