class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # start with minimum length as positive infinity - the 1st valid
        # subarray will be smaller than it
        # my thinking - keep expanding sliding window to the right
        # until you have a valid window
        # then keep shrinking the window from the left until it is
        # invalid, then repeat the process again
        # in current window, track running total of all nums in window

        # variable for minimum length
        min_length = float('infinity')

        # sliding window requires left and right pointers
        left = 0

        # determine size of input array
        n = len(nums)

        # track sum of current window to compare with target
        total = 0
        
        # right pointer iterates through the whole array
        for right in range(n):
            # window is invalid
            total += nums[right]

            # while the window is valid, shrink from left and
            # increment left pointer
            while total >= target:
                # update min_length
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1

        # no valid subarray if min_length is still infinite
        return min_length if min_length != float('infinity') else 0
