class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0

        if not nums:
            return max_ones

        ones = 0
        for num in nums:
            if num != 1:
                ones = 0
            else:
                ones += 1
                max_ones = max(max_ones, ones)

        return max_ones