class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        right_maxes = [0] * n
        right_max = 0

        for i in range(n - 1, -1, -1):
            right_maxes[i] = right_max
            right_max = max(right_max, height[i])
        
        left_max = height[0]
        water = 0

        for j in range(1, n - 1):
            water += max(0, min(left_max, right_maxes[j]) - height[j])
            left_max = max(left_max, height[j])

        return water

