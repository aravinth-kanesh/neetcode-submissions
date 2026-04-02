class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # return empty list if list smaller than k
        if len(nums) < k:
            return []

        # store maxes of each window
        res = []
        # store indices of nums
        q = deque()

        # initialise sliding window
        left = 0
        for right in range(len(nums)):
            # pop back of q elements that can never be max of window
            while q and nums[q[-1]] <= nums[right]:
                q.pop()

            # add index of num at right pointer
            q.append(right)

            # remove index out of window
            if q[0] < left:
                q.popleft()

            # when window is k size, add max of window which is front
            if right - left + 1 == k:
                res.append(nums[q[0]])
                # increment left pointer
                left += 1

        return res