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

    # koko needs to eat all the bananas within h number of hours. The worst
    # case is that h is the length of the piles, and so koko would have
    # to eat eat pile in 1 hour. This can only be done if koko eats at a 
    # rate of max(piles) an hour. The best case is 1, and so this is the 
    # lower bound. We can do a brute force of every possible banana eating
    # rate in this range, but that would make the complexity O(n^2). We
    # can do this more efficiently using a binary search approach. After
    # calculating the midpoint, we see how long it takes to eat all the 
    # piles at midpoint bananas eaten per hour. We then compare this with
    # the max allowed time which is h. If it is less than it, then we 
    # have found a local min, and so update the result variable. But we 
    # have a better solution, the global min, and so we carry on the
    # binary search by setting the right pointer to mid - 1. Otherwise,
    # the time exceeded h and so the min eating rate must be higher than
    # the midpoint, as so we set left to mid + 1. This algorithm is more
    # efficient, and eventually it will land on the global minimum.
    
