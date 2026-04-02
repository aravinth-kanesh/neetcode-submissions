import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        if len(piles) == h:
            return res

        while left <= right:
            time = 0
            mid = (left + right) // 2

            for pile in piles:
                time += math.ceil(pile / mid)

            if time <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
