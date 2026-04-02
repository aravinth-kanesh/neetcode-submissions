class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        max_water = 0

        left, right = 0, len(heights) - 1
        while left < right:
            # adjust pointers while heights are invalid
            while heights[left] < 0:
                left += 1
            while heights[right] < 0:
                right -= 1

            water = min(heights[left], heights[right]) * (right - left)
            max_water = max(max_water, water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water

        # time - O(n), which is good

        # space - O(1)