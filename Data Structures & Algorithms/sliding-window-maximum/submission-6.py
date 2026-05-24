class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0] * ((len(nums) - k) + 1)
        l, r = 0, k - 1

        for i in range(len(res)):
            res[i] = max(nums[l:r + 1])
            l += 1
            r += 1

        return res