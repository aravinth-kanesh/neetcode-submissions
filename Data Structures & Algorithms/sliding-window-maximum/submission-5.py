class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []

        res = []
        q = deque() # monotonic queue to store indices

        left = 0
        for right in range(len(nums)):
            # pop elements that can never be window maximum
            while q and nums[q[-1]] <= nums[right]:
                q.pop()

            # add right of window to queue
            q.append(right)

            # remove elements outside of sliding window
            if q[0] < left:
                q.popleft()

            # add window maximum to res
            if (right - left + 1) >= k:
                res.append(nums[q[0]])
                left += 1

        return res