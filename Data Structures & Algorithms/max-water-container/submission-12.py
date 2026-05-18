class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left, right = 0, len(heights) - 1

        # do not want the bars to overlap, hence not <=
        while left < right:
            water = min(heights[left], heights[right]) * (right - left)
            max_water = max(water, max_water)

            if heights[left] < heights[right]:
                # try to find a taller bar, at the expense of
                # making the width smalelr
                left += 1
            else:
                right -= 1

        return max_water