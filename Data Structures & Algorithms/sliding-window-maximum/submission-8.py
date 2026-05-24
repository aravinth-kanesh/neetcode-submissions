class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # stores indices
        res = []

        left = 0
        for right in range(len(nums)):
            # can never be sliding window maximum anyways
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            # add new index
            queue.append(right)

            # pop index out of window
            if queue[0] < left:
                queue.popleft()

            # compute window maximum
            if right + 1 >= k:
                res.append(nums[queue[0]])
                left += 1

        return res
