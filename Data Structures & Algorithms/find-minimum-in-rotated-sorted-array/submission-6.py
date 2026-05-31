class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        # use binary seach
        left = 0
        right = len(nums) - 1

        while left <= right:
            # need to check if mid in left sorted portion or right sorted portion
            # key insight - all nums in left sorted portion greater than all nums
            # in right sorted portion

            # also need to check if search space is already sorted
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])

            # mid is in left sorted portion
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                # mid is in right sorted portion
                right = mid - 1

        return res