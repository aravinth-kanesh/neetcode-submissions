class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            # check if duplicate exists
            if num in seen and i - seen[num] <= k:
                return True

            # add it to the seen hashmap (or update)
            seen[num] = i

        # nothing satisfies the condition
        return False
