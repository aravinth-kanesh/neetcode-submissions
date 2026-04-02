class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # hashmap mapping each unique number to their occurrence
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # sort the hashmap by the frequency, ensure to set reverse to True
        # end the iterable at k elements
        top_k = sorted(count.items(), key = lambda x: x[1], reverse = True)[:k]

        # create an array with just the numbers and return
        return [num for num, freq in top_k]

