class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # nums[queue[0]] is window max at every time step >= k
        res = [] # output list

        # sliding window approach
        left = 0
        for right in range(len(nums)):
            # smaller elements can never be window max
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()

            queue.append(right)

            # remove elements out of the window (from the left)
            if queue[0] < left:
                queue.popleft()

            # window of size k formed
            if right >= k - 1:
                res.append(nums[queue[0]])
                left += 1

        return res


            