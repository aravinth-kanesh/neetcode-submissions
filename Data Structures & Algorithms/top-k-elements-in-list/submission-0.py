class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occs = {}

        for num in nums:
            if num not in occs:
                occs[num] = 1
            else:
                occs[num] += 1

        top_k = sorted(occs.items(), key = lambda x: x[1], reverse = True)[:k]

        return [num for num, occ in top_k]
