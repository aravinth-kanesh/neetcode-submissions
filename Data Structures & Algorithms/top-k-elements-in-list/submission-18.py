class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [] # min heap
        heapq.heapify(heap)

        # {1: 3, 2: 2, 3: 1} for example
        freqs = Counter(nums) # count frequency of each num

        # .items() makes it iterable
        for num, freq in freqs.items(): 
            heapq.heappush(heap, (freq, num))

            # exceeds k size
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while heap:
            freq, num = heapq.heappop(heap)
            result.append(num)

        return result

        

