class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0
        left, right = 0, len(heights) - 1

        # don't want the same bars to be considered at once,
        # hence less than instead of less than or equal to
        while left < right:
            # water will start flowing out above the smaller bar
            water = min(heights[left], heights[right]) * (right - left)
            # update most_water var
            most_water = max(most_water, water)

            if heights[left] < heights[right]:
                # increment left pointer to find a larger bar
                left += 1
            else:
                # decrement right pointer to find a smaller bar
                right -= 1

        return most_water
