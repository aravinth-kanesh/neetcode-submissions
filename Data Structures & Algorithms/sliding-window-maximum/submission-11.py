class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []

        left = 0
        for right in range(len(nums)):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            queue.append(right)

            if queue[0] < left:
                queue.popleft()

            if right >= k - 1:
                res.append(nums[queue[0]])
                left += 1

        return res