class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. create a frequency map of nums
        freqs = dict(Counter(nums))

        # example: [1,2,2,3,3,3], k = 2
        # freqs = {1: 1, 2: 2, 3: 3}

        # 2. sort the frequency map
        # expected output of [3, 2] or [2, 3]

        # build a min heap
        heap = []

        # push all (num, freq) pairs onto the heap
        for num, freq in freqs.items():
            heapq.heappush(heap, (freq, num))
            # pop from heap when it exceeds k number of elements
            # this keeps the heap k elements large
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]