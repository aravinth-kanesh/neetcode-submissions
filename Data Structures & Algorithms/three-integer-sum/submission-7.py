class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # loop through every number
        # initialise two-pointer solution for rest of array after
        # current pointer

        # sort the input array so that two-pointer approach is
        # valid
        nums.sort()

        # store all unique triplets
        res = []

        # length of array
        n = len(nums)

        for i in range(n):
            # skip over duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # intialise two-pointer approach
            left, right = i + 1, n - 1

            # keep iterating while pointers do not cross over
            while left < right:
                # sum the triplet
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    # need to make the sum larger, so increment left
                    left += 1
                elif total > 0:
                    # need to make the sum smaller, so decrement right
                    right -= 1
                else:
                    # otherwise a valid triplet has been found
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # increment pointers to skip over duplicates
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res

        # time is O(n) for outer loop, O(n) for inner loop, so O(n^2)
        # space is O(m) for the output list
