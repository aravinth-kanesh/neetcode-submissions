class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums)

        def rob_linear(arr):
            m = len(arr)

            dp = [0] * m
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, m):
                dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])

            return dp[-1]

        return max(rob_linear(nums[:n - 1]), rob_linear(nums[1:]))