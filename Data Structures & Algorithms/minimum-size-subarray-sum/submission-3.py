class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('infinity')

        left = total = 0
        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                # update min_length
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1

        return min_length if min_length != float('infinity') else 0