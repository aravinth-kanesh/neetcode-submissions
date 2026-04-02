class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        total = 0

        # calculate left max at each position
        leftMax = [0] * n
        left = 0
        for i in range(n):
            leftMax[i] = left
            left = max(left, height[i])

        # calculate right max at each position
        rightMax = [0] * n
        right = 0
        for i in range(n - 1, -1, -1):
            rightMax[i] = right
            right = max(right, height[i])

        print(leftMax)
        print(rightMax)

        # for each position, it is easy to see that the amount of
        # water trapped there is the min(leftMax, rightMax) - height
        for i in range(n):
            total += max(0, (min(leftMax[i], rightMax[i]) - height[i]))

        return total
        
