class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array for two pointer solution to work
        nums.sort()

        result = []

        # edge case - nums is empty
        if not nums:
            return result

        # loop through every number in the array
        # for every number, do a 2 pointer approach on the remaining nums

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
