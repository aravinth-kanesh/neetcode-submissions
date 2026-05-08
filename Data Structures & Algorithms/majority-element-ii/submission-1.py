class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        freqs = Counter(nums)
        target_freq = len(nums) // 3 + 1

        for num, freq in freqs.items():
            if freq >= target_freq:
                res.append(num)

        return res

