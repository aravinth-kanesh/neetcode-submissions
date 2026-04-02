class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # return empty list if k larger than the list
        if len(nums) < k:
            return []

        # store max element at each step
        res = []
        # store numbers in current window
        window = deque()

        # initialise sliding window
        left = right = 0
        while right < len(nums):
            # increase the window size until k
            # this only happens at the beginning
            while right - left + 1 < k:
                window.append(nums[right])
                right += 1

            # add new element to the sliding window
            window.append(nums[right])

            # add max element to window
            res.append(max(window))

            # pop leftmost element
            window.popleft()

            # shift window
            left += 1
            right += 1

        return res