class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # eating rate needed to eat each pile in 1 hour in max(piles)
        # binary search from 1 to max(piles)
        left = 1
        right = k = max(piles)

        if k == h:
            return k

        while left <= right:
            mid = (left + right) // 2
            time = sum(math.ceil(pile / mid) for pile in piles)

            if time <= h:
                # try to find smaller solution
                k = mid
                right = mid - 1
            else:
                # cannot update k, solution is larger
                left = mid + 1

        return k