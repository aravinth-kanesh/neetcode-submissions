class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build frequency map
        freq_map = Counter(nums)

        # create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # populate buckets
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        top_k = []
        # traverse buckets right to left
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k