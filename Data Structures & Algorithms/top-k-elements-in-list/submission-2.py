class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        top_k = sorted(nums_count.items(), key = lambda x: x[1], reverse = True)[:k]
        return [num for num, count in top_k]