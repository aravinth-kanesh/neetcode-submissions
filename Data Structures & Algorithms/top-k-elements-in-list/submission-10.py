class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # for example 1: will give us {1: 1, 2: 2, 3: 3}
        freqs = Counter(nums)
        freqs_heap = [(freq, num) for num, freq in freqs.items()]
        # heapq.heapify(freqs_heap)
        return [num for freq, num in heapq.nlargest(k, freqs_heap)]