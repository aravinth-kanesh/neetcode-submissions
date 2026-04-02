class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a brute force solution would be to have three nested
        # loops, and see if the combination of elements sum up
        # to 0 - problem - O(n^3) time complexity
        # O(nlogn) time complexity - uses the Timsort algorithm
        res = []
        nums.sort()

        # loops through every number in the array - n iterations
        # for each number, n operations in the worst case
        # n x n which is O(n^2) time complexity
        # space - excluding the results array, pointer variables
        # are constant space - O(1). If we are including the res
        # array, then space is O(n)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    # need to make the total larger
                    # increment left
                    left += 1
                elif total > 0:
                    # need to make the total smaller
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # [0, 1, 3, 4, 4, 5]
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res

