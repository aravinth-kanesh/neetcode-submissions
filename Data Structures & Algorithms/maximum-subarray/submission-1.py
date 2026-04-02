class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_total, total = 0, nums[0]

        for num in nums:
            if current_total < 0:
                current_total = 0

            current_total += num
            total = max(current_total, total)

        return total