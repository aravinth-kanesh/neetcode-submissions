class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # target found
            if nums[mid] == target:
                return mid

            # mid is in left sorted portion
            if nums[mid] >= nums[left]:
                # target is in left sorted portion
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # target is in right sorted portion
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


            