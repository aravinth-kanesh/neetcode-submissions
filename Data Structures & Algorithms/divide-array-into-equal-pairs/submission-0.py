class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freqs = Counter(nums)

        for freq in freqs.values():
            # odd frequency
            if freq % 2 == 1:
                return False

        # all frequencies are even
        return True