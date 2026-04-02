class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_occs = Counter(nums)
        # top_k = sorted(num_occs.items(), key = lambda x: x[1], reverse = True)[:k]
        # return [num for num, occ in top_k]
        return [num for num, occ in heapq.nlargest(k, num_occs.items(), key = lambda x: x[1])]
