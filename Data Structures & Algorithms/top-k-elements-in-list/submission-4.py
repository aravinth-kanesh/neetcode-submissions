class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        # gives us each number mapped to their frequency
        # e.g. {1: 2, 2: 2, 3: 3}

        top_k = sorted(count.items(), key = lambda x: x[1], reverse = True)[:k]

        # gives us {3: 3, 2: 2, 1: 1}

        return [num for num, occ in top_k]