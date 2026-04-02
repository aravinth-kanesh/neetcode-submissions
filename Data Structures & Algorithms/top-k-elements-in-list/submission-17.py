class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        return heapq.nlargest(k, freqs.keys(), key=freqs.get)