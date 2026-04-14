class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_bound = (len(nums) // 2) + 1
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1
            if freqs[num] == majority_bound:
                return num